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
    PollHandler,
    CallbackQueryHandler,
)
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
    await update.message.reply_text(
        "Привет! 👋 Я твой личный ИИ-тренажер по программированию.\n\n"
        "Все команды доступны в меню слева. ⬇️"
    )

async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows category selection buttons."""
    keyboard = [
        [InlineKeyboardButton("🐍 Python", callback_data="cat_python"), InlineKeyboardButton("🛠 Git", callback_data="cat_git")],
        [InlineKeyboardButton("💻 Terminal", callback_data="cat_terminal"), InlineKeyboardButton("🎨 HTML/CSS", callback_data="cat_html_css")],
        [InlineKeyboardButton("🌐 SSH/OS", callback_data="cat_ssh_os"), InlineKeyboardButton("🎲 Всё вперемешку", callback_data="cat_all")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери тему:", reply_markup=reply_markup)

async def category_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    category = query.data.replace("cat_", "")
    context.user_data["temp_category"] = category
    context.user_data["is_blitz"] = False
    
    keyboard = [
        [InlineKeyboardButton("🟢 Легко", callback_data="diff_easy")],
        [InlineKeyboardButton("🟡 Средне", callback_data="diff_medium")],
        [InlineKeyboardButton("🔴 Хард", callback_data="diff_hard")],
        [InlineKeyboardButton("🌈 Любая сложность", callback_data="diff_any")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(f"Тема: {category.upper()}\nВыбери уровень сложности:", reply_markup=reply_markup)

async def difficulty_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    difficulty = query.data.replace("diff_", "")
    context.user_data["menu_message_id"] = query.message.message_id
    await start_quiz_logic(query.message, context, difficulty)

async def start_blitz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts blitz mode."""
    context.user_data["is_blitz"] = True
    context.user_data["temp_category"] = "all"
    await start_quiz_logic(update.message, context, "any")

async def start_quiz_logic(message, context, difficulty):
    category = context.user_data.get("temp_category", "all")
    is_blitz = context.user_data.get("is_blitz", False)
    user_id = message.chat_id # In private chats chat_id == user_id
    
    if category == "all":
        filtered = QUIZ_DATA
    elif category == "ssh_os":
        filtered = [q for q in QUIZ_DATA if q["category"] in ["ssh", "os"]]
    else:
        filtered = [q for q in QUIZ_DATA if q["category"] == category]
        
    if difficulty != "any":
        filtered = [q for q in filtered if q["difficulty"] == difficulty]

    if not filtered:
        await message.reply_text("Вопросов не найдено. Выбери другое!")
        return

    num_q = min(10, len(filtered))
    user_questions = random.sample(filtered, num_q)
    
    context.user_data["questions"] = user_questions
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    context.user_data["chat_id"] = user_id
    context.user_data["user_id"] = user_id
    context.user_data["category_name"] = "blitz" if is_blitz else category
    context.user_data["difficulty_name"] = difficulty
    
    menu_id = context.user_data.get("menu_message_id")
    if menu_id:
        try: await context.bot.delete_message(chat_id=user_id, message_id=menu_id)
        except: pass

    await send_next_poll(context)

async def start_errors_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    error_texts = get_user_errors(chat_id)
    if not error_texts:
        await update.message.reply_text("Ошибок нет! ✨")
        return
    error_questions = [q for q in QUIZ_DATA if q["question"] in error_texts]
    random.shuffle(error_questions)
    context.user_data["questions"] = error_questions[:10]
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    context.user_data["chat_id"] = chat_id
    context.user_data["user_id"] = chat_id
    context.user_data["category_name"] = "errors"
    context.user_data["difficulty_name"] = "review"
    context.user_data["is_blitz"] = False
    await send_next_poll(context)

async def send_next_poll(context: ContextTypes.DEFAULT_TYPE):
    index = context.user_data.get("current_question", 0)
    questions = context.user_data.get("questions", [])
    chat_id = context.user_data.get("chat_id")
    user_id = context.user_data.get("user_id")
    is_blitz = context.user_data.get("is_blitz", False)

    if not questions or index >= len(questions):
        score = context.user_data.get("score", 0)
        update_user_stats(chat_id, context.user_data.get("username", "User"), score, len(questions), 
                         context.user_data.get("category_name"), context.user_data.get("difficulty_name"))
        await context.bot.send_message(chat_id=chat_id, text=f"🏁 Окончено! Результат: {score}/{len(questions)}.")
        return

    question_data = questions[index]
    open_period = 20 if is_blitz else None

    try:
        message = await context.bot.send_poll(
            chat_id=chat_id,
            question=f"[{index + 1}/{len(questions)}] {question_data['question']}",
            options=question_data["options"],
            type=Poll.QUIZ,
            correct_option_id=question_data["correct_index"],
            explanation=question_data["explanation"],
            is_anonymous=False,
            open_period=open_period,
        )
        # Store metadata to track poll progress
        context.bot_data[message.poll.id] = {
            "chat_id": chat_id,
            "user_id": user_id,
            "correct_option_id": question_data["correct_index"],
            "question_text": question_data["question"],
            "question_index": index
        }
    except Exception as e:
        logging.error(f"Error: {e}")
        await send_next_poll(context)

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles when user actually clicks an answer."""
    answer = update.poll_answer
    poll_info = context.bot_data.get(answer.poll_id)
    if not poll_info: return

    user_id = poll_info["user_id"]
    user_data = context.application.user_data.get(user_id)
    if not user_data: return

    # Check if we already processed this question (to avoid double trigger from PollHandler)
    if user_data.get("current_question") != poll_info["question_index"]:
        return

    question_text = poll_info["question_text"]
    user_data["username"] = answer.user.first_name

    if answer.option_ids and answer.option_ids[0] == poll_info["correct_option_id"]:
        user_data["score"] = user_data.get("score", 0) + 1
        remove_wrong_answer(user_id, question_text)
    else:
        add_wrong_answer(user_id, question_text)

    user_data["current_question"] += 1
    
    # Remove poll from memory and move to next
    context.bot_data.pop(answer.poll_id, None)
    
    # We need a new context-like object for the next poll call since we are in a different handler
    # Actually, we can just use a helper function that takes user_data
    await send_next_poll_custom(context, user_data)

async def handle_poll_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles when poll state changes (e.g. closed by timer)."""
    poll = update.poll
    if not poll.is_closed:
        return

    poll_info = context.bot_data.get(poll.id)
    if not poll_info:
        return

    user_id = poll_info["user_id"]
    user_data = context.application.user_data.get(user_id)
    if not user_data:
        return

    # If time ran out and user didn't answer
    if user_data.get("current_question") == poll_info["question_index"]:
        # Count as wrong answer
        add_wrong_answer(user_id, poll_info["question_text"])
        user_data["current_question"] += 1
        
        context.bot_data.pop(poll.id, None)
        await send_next_poll_custom(context, user_data)

async def send_next_poll_custom(context, user_data):
    """Helper to send next poll using stored user_data."""
    # We temporarily inject user_data into a dummy context to reuse send_next_poll logic
    # Or just write a slightly more flexible version
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
            chat_id=chat_id,
            question=f"[{index + 1}/{len(questions)}] {question_data['question']}",
            options=question_data["options"],
            type=Poll.QUIZ,
            correct_option_id=question_data["correct_index"],
            explanation=question_data["explanation"],
            is_anonymous=False,
            open_period=open_period,
        )
        context.bot_data[message.poll.id] = {
            "chat_id": chat_id,
            "user_id": user_data.get("user_id"),
            "correct_option_id": question_data["correct_index"],
            "question_text": question_data["question"],
            "question_index": index
        }
    except Exception as e:
        logging.error(f"Error: {e}")

# ... (stats, top, subscribe stay same) ...
async def daily_question(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    question_data = random.choice(QUIZ_DATA)
    await context.bot.send_message(chat_id=chat_id, text="⏰ Вопрос дня!")
    await context.bot.send_poll(chat_id=chat_id, question=question_data['question'], options=question_data['options'], 
                               type=Poll.QUIZ, correct_option_id=question_data['correct_index'], 
                               explanation=question_data['explanation'], is_anonymous=False)

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    jobs = context.job_queue.get_jobs_by_name(str(chat_id))
    for job in jobs: job.schedule_removal()
    context.job_queue.run_daily(daily_question, time=time(10, 0, 0), chat_id=chat_id, name=str(chat_id))
    await update.message.reply_text("✅ Подписан!")

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

if __name__ == "__main__":
    if not TOKEN: exit(1)
    app = ApplicationBuilder().token(TOKEN).post_init(post_init).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", show_categories))
    app.add_handler(CommandHandler("blitz", start_blitz))
    app.add_handler(CommandHandler("errors", start_errors_quiz))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("top", top))
    app.add_handler(CommandHandler("subscribe", subscribe))
    
    app.add_handler(CallbackQueryHandler(category_callback, pattern="^cat_"))
    app.add_handler(CallbackQueryHandler(difficulty_callback, pattern="^diff_"))
    
    # Handlers for Polls
    app.add_handler(PollAnswerHandler(handle_poll_answer)) # When user answers
    app.add_handler(PollHandler(handle_poll_update))     # When poll state changes (e.g. timeout)
    
    print("Бот в разработке (Blitz Timeout Fixed)...")
    app.run_polling()
