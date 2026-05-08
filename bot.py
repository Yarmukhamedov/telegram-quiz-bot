import os
import logging
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
        "Я готов протестировать твои знания в формате викторины.\n"
        "Просто выбери правильный вариант в опросе!\n\n"
        "Используй /quiz, чтобы начать."
    )
    await update.message.reply_text(text)

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the quiz."""
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    await send_next_poll(update, context)

async def send_next_poll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the next question as a native Telegram Poll (Quiz)."""
    index = context.user_data.get("current_question", 0)
    
    if index >= len(QUIZ_DATA):
        # Quiz finished
        score = context.user_data.get("score", 0)
        total = len(QUIZ_DATA)
        await context.bot.send_message(
            chat_id=context.user_data["chat_id"],
            text=f"🏁 Викторина окончена!\nТвой результат: {score} из {total}.\n\nЧтобы пройти еще раз, нажми /quiz."
        )
        return

    question_data = QUIZ_DATA[index]
    
    # We need chat_id to send messages later. PollAnswer update doesn't have it.
    if update.message:
        chat_id = update.message.chat_id
        context.user_data["chat_id"] = chat_id
    else:
        chat_id = context.user_data["chat_id"]

    message = await context.bot.send_poll(
        chat_id=chat_id,
        question=f"[{index + 1}/{len(QUIZ_DATA)}] {question_data['question']}",
        options=question_data["options"],
        type=Poll.QUIZ,
        correct_option_id=question_data["correct_index"],
        explanation=question_data["explanation"],
        is_anonymous=False, # Set to False to get PollAnswer updates
    )
    
    # Store poll info to track progress
    payload = {
        message.poll.id: {
            "chat_id": chat_id,
            "user_id": update.effective_user.id,
            "correct_option_id": question_data["correct_index"]
        }
    }
    context.bot_data.update(payload)

async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the user's answer to the poll."""
    answer = update.poll_answer
    poll_id = answer.poll_id
    
    # Get stored poll info
    poll_info = context.bot_data.get(poll_id)
    if not poll_info:
        return

    user_id = answer.user.id
    selected_option = answer.option_ids[0]
    
    # Update score if correct
    if selected_option == poll_info["correct_option_id"]:
        context.user_data["score"] = context.user_data.get("score", 0) + 1

    # Move to next question
    context.user_data["current_question"] = context.user_data.get("current_question", 0) + 1
    
    # Small delay or just send next
    await send_next_poll(update, context)

if __name__ == "__main__":
    if not TOKEN:
        print("Ошибка: Переменная окружения TELEGRAM_TOKEN не задана!")
        exit(1)
        
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quiz", start_quiz))
    app.add_handler(PollAnswerHandler(handle_poll_answer))
    
    print("Бот (Poll Mode) запущен...")
    app.run_polling()
