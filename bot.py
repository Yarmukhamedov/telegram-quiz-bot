import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    ConversationHandler,
)
from questions import QUIZ_DATA

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# States for ConversationHandler
QUIZ_STATE = range(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Welcome message."""
    user = update.effective_user
    text = (
        f"Привет, {user.first_name}! 👋\n\n"
        "Я бот для тестирования твоих знаний в программировании. "
        "Я составил вопросы на основе твоих недавних занятий.\n\n"
        "Используй /quiz, чтобы начать тест!"
    )
    await update.message.reply_text(text)

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the quiz."""
    context.user_data["current_question"] = 0
    context.user_data["score"] = 0
    
    await send_question(update, context)
    return QUIZ_STATE

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the current question to the user."""
    index = context.user_data["current_question"]
    question_data = QUIZ_DATA[index]
    
    keyboard = []
    for i, option in enumerate(question_data["options"]):
        keyboard.append([InlineKeyboardButton(option, callback_data=str(i))])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    text = f"Вопрос {index + 1}/{len(QUIZ_DATA)}:\n\n{question_data['question']}"
    
    if update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the answer selected by the user."""
    query = update.callback_query
    await query.answer()
    
    selected_index = int(query.data)
    current_index = context.user_data["current_question"]
    question_data = QUIZ_DATA[current_index]
    
    is_correct = selected_index == question_data["correct_index"]
    
    if is_correct:
        context.user_data["score"] += 1
        result_text = "✅ Верно!"
    else:
        result_text = "❌ Неверно."
    
    explanation = f"\n\n💡 {question_data['explanation']}"
    
    # Show feedback and move to next or finish
    context.user_data["current_question"] += 1
    
    if context.user_data["current_question"] < len(QUIZ_DATA):
        # Add a "Next" button
        keyboard = [[InlineKeyboardButton("Следующий вопрос ➡️", callback_data="next")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(f"{result_text}{explanation}", reply_markup=reply_markup)
        return QUIZ_STATE
    else:
        # Finish quiz
        score = context.user_data["score"]
        total = len(QUIZ_DATA)
        final_text = (
            f"{result_text}{explanation}\n\n"
            "🏁 Тест окончен!\n"
            f"Твой результат: {score} из {total}.\n\n"
            "Молодец! Продолжай учиться. Чтобы пройти снова, нажми /quiz."
        )
        await query.edit_message_text(final_text)
        return ConversationHandler.END

async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Triggered when user clicks 'Next'."""
    query = update.callback_query
    await query.answer()
    await send_question(update, context)
    return QUIZ_STATE

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Cancels the conversation."""
    await update.message.reply_text("Тест отменен. Если захочешь продолжить, введи /quiz.")
    return ConversationHandler.END

if __name__ == "__main__":
    if not TOKEN:
        print("Ошибка: Переменная окружения TELEGRAM_TOKEN не задана!")
        exit(1)
        
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Conversation handler for the quiz
    quiz_handler = ConversationHandler(
        entry_points=[CommandHandler("quiz", start_quiz)],
        states={
            QUIZ_STATE: [
                CallbackQueryHandler(next_question, pattern="^next$"),
                CallbackQueryHandler(handle_answer),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(quiz_handler)
    
    print("Бот запущен...")
    app.run_polling()
