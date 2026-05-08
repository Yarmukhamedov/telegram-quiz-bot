import os
import logging
import random
import asyncio
from dotenv import load_dotenv
from telegram import Update, Poll
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
)
from questions import QUIZ_DATA

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message."""
    await update.message.reply_text(
        "Привет! 👋 Я готов к викторине.\n\n"
        "Нажми /quiz, чтобы начать!"
    )

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the quiz with randomized questions."""
    # Randomize questions for this session
    user_questions = random.sample(QUIZ_DATA, len(QUIZ_DATA))
    
    context.user_data["questions"] = user_questions
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    context.user_data["chat_id"] = update.effective_chat.id
    
    await send_next_poll(update, context)

async def send_next_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the next question."""
    index = context.user_data.get("current_question", 0)
    questions = context.user_data.get("questions", [])
    chat_id = context.user_data.get("chat_id")

    if not questions or index >= len(questions):
        score = context.user_data.get("score", 0)
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"🏁 Викторина окончена!\n\nТвой результат: {score} из {len(questions)}.\n\nЧтобы пройти еще раз, нажми /quiz."
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
            "user_id": update.effective_user.id,
            "correct_option_id": question_data["correct_index"]
        }
    except Exception as e:
        logging.error(f"Failed to send poll: {e}")
        # Basic retry logic for network fluctuations
        await asyncio.sleep(1)
        await send_next_poll(update, context)

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the user's answer."""
    answer = update.poll_answer
    poll_info = context.bot_data.get(answer.poll_id)
    if not poll_info:
        return

    if answer.option_ids[0] == poll_info["correct_option_id"]:
        context.user_data["score"] = context.user_data.get("score", 0) + 1

    context.user_data["current_question"] = context.user_data.get("current_question", 0) + 1
    await send_next_poll(update, context)

if __name__ == "__main__":
    if not TOKEN:
        print("Error: TELEGRAM_TOKEN not found in .env")
        exit(1)
        
    # Standard application build (no proxy)
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", start_quiz))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
    
    print("Бот запущен (Clean Mode)...")
    app.run_polling()
