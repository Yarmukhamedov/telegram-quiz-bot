import os
import logging
import random
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
    user = update.effective_user
    text = (
        f"Привет, {user.first_name}! 👋\n\n"
        "Я готов протестировать твои знания. Теперь вопросов стало больше, и они всегда идут в случайном порядке!\n\n"
        "Используй /quiz, чтобы начать."
    )
    await update.message.reply_text(text)

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the quiz with randomized questions."""
    # Create a randomized copy of questions for this specific session
    user_questions = random.sample(QUIZ_DATA, len(QUIZ_DATA))
    
    context.user_data["questions"] = user_questions
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    context.user_data["chat_id"] = update.effective_chat.id
    
    await send_next_poll(update, context)

async def send_next_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the next question from the randomized list."""
    index = context.user_data.get("current_question", 0)
    questions = context.user_data.get("questions", [])
    chat_id = context.user_data.get("chat_id")

    if not questions or index >= len(questions):
        # Quiz finished
        score = context.user_data.get("score", 0)
        total = len(questions) if questions else len(QUIZ_DATA)
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"🏁 Викторина окончена!\n\nТвой результат: {score} из {total}.\n\nЧтобы пройти еще раз со случайными вопросами, нажми /quiz."
        )
        # Clear data
        context.user_data["questions"] = []
        return

    question_data = questions[index]
    
    message = await context.bot.send_poll(
        chat_id=chat_id,
        question=f"[{index + 1}/{len(questions)}] {question_data['question']}",
        options=question_data["options"],
        type=Poll.QUIZ,
        correct_option_id=question_data["correct_index"],
        explanation=question_data["explanation"],
        is_anonymous=False,
    )
    
    # Map poll_id to user to track answers
    payload = {
        message.poll.id: {
            "user_id": update.effective_user.id,
            "correct_option_id": question_data["correct_index"]
        }
    }
    context.bot_data.update(payload)

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the user's answer and triggers next question."""
    answer = update.poll_answer
    poll_id = answer.poll_id
    
    poll_info = context.bot_data.get(poll_id)
    if not poll_info:
        return

    # Check if correct
    selected_option = answer.option_ids[0]
    if selected_option == poll_info["correct_option_id"]:
        context.user_data["score"] = context.user_data.get("score", 0) + 1

    # Move index forward
    context.user_data["current_question"] = context.user_data.get("current_question", 0) + 1
    
    # Small delay for better UX (optional)
    await send_next_poll(update, context)

if __name__ == "__main__":
    if not TOKEN:
        print("Ошибка: Переменная окружения TELEGRAM_TOKEN не задана!")
        exit(1)
        
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", start_quiz))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
    
    print("Бот (Randomized Mode) запущен...")
    app.run_polling()
