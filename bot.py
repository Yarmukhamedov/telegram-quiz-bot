import os
import logging
import random
import asyncio
from dotenv import load_dotenv
from telegram import Update, Poll, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
    CallbackQueryHandler,
)
from questions import QUIZ_DATA
from database import init_db, update_user_stats, get_user_stats, get_top_users

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Initialize Database
init_db()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message."""
    await update.message.reply_text(
        "Привет! 👋 Я твой продвинутый тренажер по программированию.\n\n"
        "Я теперь умею:\n"
        "📊 Вести твою статистику (/stats)\n"
        "🏆 Показывать лидеров (/top)\n"
        "Выбирай категорию и погнали!\n\n"
        "Нажми /quiz, чтобы выбрать категорию."
    )

async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows category selection buttons."""
    keyboard = [
        [
            InlineKeyboardButton("🐍 Python", callback_data="cat_python"),
            InlineKeyboardButton("🛠 Git", callback_data="cat_git"),
        ],
        [
            InlineKeyboardButton("💻 Terminal", callback_data="cat_terminal"),
            InlineKeyboardButton("🎨 HTML/CSS", callback_data="cat_html_css"),
        ],
        [
            InlineKeyboardButton("🌐 SSH/OS", callback_data="cat_ssh_os"),
            InlineKeyboardButton("🎲 Всё вперемешку", callback_data="cat_all"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери тему викторины:", reply_markup=reply_markup)

async def category_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles category selection and starts quiz."""
    query = update.callback_query
    await query.answer()
    
    category = query.data.replace("cat_", "")
    
    # Filter questions based on category
    if category == "all":
        filtered_questions = QUIZ_DATA
    elif category == "ssh_os":
        filtered_questions = [q for q in QUIZ_DATA if q["category"] in ["ssh", "os"]]
    else:
        filtered_questions = [q for q in QUIZ_DATA if q["category"] == category]

    if not filtered_questions:
        await query.edit_message_text("В этой категории пока нет вопросов. Выбери другую!")
        return

    # Shuffle and pick 10 questions (or less if not enough)
    num_q = min(10, len(filtered_questions))
    user_questions = random.sample(filtered_questions, num_q)
    
    context.user_data["questions"] = user_questions
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    context.user_data["chat_id"] = query.message.chat_id
    context.user_data["category_name"] = category
    
    await query.edit_message_text(f"Начинаем викторину по теме: {category.upper()}! 🚀")
    await send_next_poll(context)

async def send_next_poll(context: ContextTypes.DEFAULT_TYPE):
    """Sends the next question."""
    index = context.user_data.get("current_question", 0)
    questions = context.user_data.get("questions", [])
    chat_id = context.user_data.get("chat_id")

    if not questions or index >= len(questions):
        score = context.user_data.get("score", 0)
        category = context.user_data.get("category_name", "all")
        
        # Save to Database
        update_user_stats(
            user_id=chat_id, # Using chat_id as user_id for simplicity in private chats
            username=context.user_data.get("username", "User"),
            score=score,
            total_questions=len(questions),
            category=category,
            difficulty="mixed"
        )
        
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"🏁 Викторина окончена!\n\nТвой результат: {score} из {len(questions)}.\n\n"
                 f"Результат сохранен в твою статистику (/stats)!"
        )
        return

    question_data = questions[index]
    
    try:
        message = await context.bot.send_poll(
            chat_id=chat_id,
            question=f"[{index + 1}/{len(questions)}] {question_data['question']}",
            options=question_data["options"],
            type=Poll.QUIZ,
            correct_option_id=question_data["correct_index"],
            explanation=question_data["explanation"],
            is_anonymous=False,
        )
        
        # Track poll for answer checking
        context.bot_data[message.poll.id] = {
            "chat_id": chat_id,
            "correct_option_id": question_data["correct_index"]
        }
    except Exception as e:
        logging.error(f"Failed to send poll: {e}")
        await asyncio.sleep(1)
        await send_next_poll(context)

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the user's answer."""
    answer = update.poll_answer
    poll_info = context.bot_data.get(answer.poll_id)
    if not poll_info:
        return

    # Update username for DB
    context.user_data["username"] = update.effective_user.first_name

    if answer.option_ids[0] == poll_info["correct_option_id"]:
        context.user_data["score"] = context.user_data.get("score", 0) + 1

    context.user_data["current_question"] = context.user_data.get("current_question", 0) + 1
    await send_next_poll(context)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows user stats."""
    user_id = update.effective_chat.id
    total_score, completed = get_user_stats(user_id)
    
    if completed == 0:
        await update.message.reply_text("Ты еще не прошел ни одной викторины! Нажми /quiz.")
    else:
        avg = round(total_score / completed, 2)
        await update.message.reply_text(
            f"📊 Твоя статистика:\n\n"
            f"✅ Пройдено тестов: {completed}\n"
            f"⭐ Всего очков: {total_score}\n"
            f"📈 Средний балл: {avg}"
        )

async def top(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Shows leaderboard."""
    top_users = get_top_users()
    if not top_users:
        await update.message.reply_text("Список лидеров пока пуст!")
        return
    
    text = "🏆 Таблица лидеров:\n\n"
    for i, (name, score) in enumerate(top_users, 1):
        text += f"{i}. {name} — {score} очков\n"
    
    await update.message.reply_text(text)

if __name__ == "__main__":
    if not TOKEN:
        print("Error: TELEGRAM_TOKEN not found in .env")
        exit(1)
        
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", show_categories))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("top", top))
    app.add_handler(CallbackQueryHandler(category_callback, pattern="^cat_"))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
    
    print("Бот в режиме разработки запущен (DB + Categories)...")
    app.run_polling()
