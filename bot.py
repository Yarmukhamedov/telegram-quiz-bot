import os
import logging
import random
import asyncio
from datetime import time
from dotenv import load_dotenv
from telegram import Update, Poll, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
    CallbackQueryHandler,
)
from telegram.request import HTTPXRequest
from questions import QUIZ_DATA
from database import (
    init_db, 
    update_user_stats, 
    get_user_stats, 
    get_top_users, 
    add_wrong_answer, 
    remove_wrong_answer, 
    get_user_errors
)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Initialize Database
init_db()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def post_init(application):
    """Sets up bot commands menu."""
    commands = [
        BotCommand("start", "🏠 Главное меню"),
        BotCommand("quiz", "🚀 Начать викторину"),
        BotCommand("blitz", "⚡️ Блиц-режим (20 сек)"),
        BotCommand("errors", "🔄 Работа над ошибками"),
        BotCommand("stats", "📊 Моя статистика"),
        BotCommand("top", "🏆 Таблица лидеров"),
        BotCommand("subscribe", "⏰ Подписка на вопрос дня"),
    ]
    await application.bot.set_my_commands(commands)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message."""
    await update.message.reply_text("Привет! 👋 Я твой личный тренажер. Все команды — в меню слева! ⬇️")

async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Dynamically generates category selection buttons from QUIZ_DATA."""
    # Get unique categories from data
    unique_cats = sorted(list(set(q["category"] for q in QUIZ_DATA)))
    
    keyboard = []
    row = []
    for i, cat in enumerate(unique_cats):
        # Create a nice label (capitalize and replace underscores)
        label = cat.replace("_", " ").capitalize()
        # Add emoji based on name if possible (optional flair)
        emoji_map = {"python": "🐍 ", "git": "🛠 ", "terminal": "💻 ", "html_css": "🎨 ", "ssh": "🌐 ", "os": "🖥 "}
        btn_text = f"{emoji_map.get(cat, '📁 ')}{label}"
        
        row.append(InlineKeyboardButton(btn_text, callback_data=f"cat_{cat}"))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row: keyboard.append(row)
    
    # Always add "All" option
    keyboard.append([InlineKeyboardButton("🎲 Всё вперемешку", callback_data="cat_all")])
    
    await update.message.reply_text("Выбери тему:", reply_markup=InlineKeyboardMarkup(keyboard))

async def category_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    category = query.data.replace("cat_", "")
    context.user_data["temp_category"] = category
    context.user_data["is_blitz"] = False
    
    keyboard = [[InlineKeyboardButton("🟢 Легко", callback_data="diff_easy")], [InlineKeyboardButton("🟡 Средне", callback_data="diff_medium")],
                [InlineKeyboardButton("🔴 Хард", callback_data="diff_hard")], [InlineKeyboardButton("🌈 Любая", callback_data="diff_any")]]
    await query.edit_message_text(f"Тема: {category.upper()}\nСложность:", reply_markup=InlineKeyboardMarkup(keyboard))

async def difficulty_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data["menu_message_id"] = query.message.message_id
    await start_quiz_logic(query.message, context, query.data.replace("diff_", ""))

async def start_blitz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["is_blitz"] = True
    context.user_data["temp_category"] = "all"
    await start_quiz_logic(update.message, context, "any")

async def start_quiz_logic(message, context, difficulty):
    category = context.user_data.get("temp_category", "all")
    is_blitz = context.user_data.get("is_blitz", False)
    user_id = message.chat_id
    
    if category == "all": 
        filtered = QUIZ_DATA
    else: 
        filtered = [q for q in QUIZ_DATA if q["category"] == category]
        
    if difficulty != "any": filtered = [q for q in filtered if q["difficulty"] == difficulty]
    if not filtered:
        await message.reply_text("Нет вопросов!")
        return

    num_q = min(10, len(filtered))
    context.user_data.update({"questions": random.sample(filtered, num_q), "current_question": 0, "score": 0, 
                             "chat_id": user_id, "user_id": user_id, "category_name": "blitz" if is_blitz else category, 
                             "difficulty_name": difficulty})
    
    menu_id = context.user_data.get("menu_message_id")
    if menu_id:
        try: await context.bot.delete_message(chat_id=user_id, message_id=menu_id)
        except: pass

    await send_next_poll(context)

async def blitz_timeout_job(context: ContextTypes.DEFAULT_TYPE):
    job_data = context.job.data
    user_id = job_data["user_id"]
    q_index = job_data["question_index"]
    user_data = context.application.user_data.get(user_id)
    if user_data and user_data.get("current_question") == q_index:
        add_wrong_answer(user_id, job_data["question_text"])
        user_data["current_question"] += 1
        await send_next_poll_custom(context, user_data)

async def send_next_poll(context: ContextTypes.DEFAULT_TYPE):
    await send_next_poll_custom(context, context.user_data)

async def send_next_poll_custom(context, user_data):
    index = user_data.get("current_question", 0)
    questions = user_data.get("questions", [])
    chat_id = user_data.get("chat_id")
    is_blitz = user_data.get("is_blitz", False)

    if not questions or index >= len(questions):
        score = user_data.get("score", 0)
        update_user_stats(chat_id, user_data.get("username", "User"), score, len(questions), 
                         user_data.get("category_name"), user_data.get("difficulty_name"))
        await context.bot.send_message(chat_id=chat_id, text=f"🏁 Окончено! Результат: {score}/{len(questions)}.")
        return

    question_data = questions[index]
    open_period = 20 if is_blitz else None
    try:
        message = await context.bot.send_poll(
            chat_id=chat_id, question=f"[{index + 1}/{len(questions)}] {question_data['question']}",
            options=question_data["options"], type=Poll.QUIZ, correct_option_id=question_data["correct_index"],
            explanation=question_data["explanation"], is_anonymous=False, open_period=open_period,
        )
        poll_id = message.poll.id
        context.bot_data[poll_id] = {"user_id": user_data.get("user_id"), "correct_option_id": question_data["correct_index"], 
                                     "question_text": question_data["question"], "question_index": index}
        if is_blitz:
            context.job_queue.run_once(blitz_timeout_job, when=22, name=f"timeout_{poll_id}", 
                                      data={"user_id": user_data.get("user_id"), "question_index": index, 
                                            "question_text": question_data["question"]})
    except Exception as e:
        logging.error(f"Error: {e}")

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = update.poll_answer
    poll_id = answer.poll_id
    poll_info = context.bot_data.get(poll_id)
    if not poll_info: return
    user_id = poll_info["user_id"]
    user_data = context.application.user_data.get(user_id)
    if not user_data or user_data.get("current_question") != poll_info["question_index"]: return
    jobs = context.job_queue.get_jobs_by_name(f"timeout_{poll_id}")
    for job in jobs: job.schedule_removal()
    user_data["username"] = answer.user.first_name
    if answer.option_ids and answer.option_ids[0] == poll_info["correct_option_id"]:
        user_data["score"] = user_data.get("score", 0) + 1
        remove_wrong_answer(user_id, poll_info["question_text"])
    else: add_wrong_answer(user_id, poll_info["question_text"])
    user_data["current_question"] += 1
    context.bot_data.pop(poll_id, None)
    await send_next_poll_custom(context, user_data)

async def start_errors_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    error_texts = get_user_errors(chat_id)
    if not error_texts:
        await update.message.reply_text("Ошибок нет! ✨")
        return
    error_questions = [q for q in QUIZ_DATA if q["question"] in error_texts]
    random.shuffle(error_questions)
    context.user_data.update({"questions": error_questions[:10], "current_question": 0, "score": 0, 
                             "chat_id": chat_id, "user_id": chat_id, "category_name": "errors", 
                             "difficulty_name": "review", "is_blitz": False})
    await send_next_poll(context)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    total_score, completed = get_user_stats(user_id)
    errors_count = len(get_user_errors(user_id))
    await update.message.reply_text(f"📊 Тестов: {completed}\n⭐ Очков: {total_score}\n❌ Ошибок: {errors_count}")

async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    top_users = get_top_users()
    if not top_users: return
    text = "🏆 Топ лидеров:\n\n"
    for i, (name, score) in enumerate(top_users, 1): text += f"{i}. {name} — {score}\n"
    await update.message.reply_text(text)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    context.job_queue.run_daily(daily_question, time=time(10, 0, 0), chat_id=chat_id, name=f"daily_{chat_id}")
    await update.message.reply_text("✅ Подписан!")

async def daily_question(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    q = random.choice(QUIZ_DATA)
    await context.bot.send_poll(chat_id=chat_id, question=q['question'], options=q['options'], type=Poll.QUIZ, 
                               correct_option_id=q['correct_index'], explanation=q['explanation'], is_anonymous=False)

if __name__ == "__main__":
    if not TOKEN: exit(1)
    request = HTTPXRequest(connect_timeout=20, read_timeout=20)
    app = ApplicationBuilder().token(TOKEN).request(request).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", show_categories))
    app.add_handler(CommandHandler("blitz", start_blitz))
    app.add_handler(CommandHandler("errors", start_errors_quiz))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("top", top))
    app.add_handler(CommandHandler("subscribe", subscribe))
    app.add_handler(CallbackQueryHandler(category_callback, pattern="^cat_"))
    app.add_handler(CallbackQueryHandler(difficulty_callback, pattern="^diff_"))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
    print("Бот в разработке (Dynamic Categories!)...")
    app.run_polling(drop_pending_updates=True)
