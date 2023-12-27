import os

from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from ask_question_from_llm import ask_question_from_llm

from consts import BOT_USERNAME, TOKEN


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there. I'm telegram assistant bot")


async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text.replace("/ask_question", "").strip()
    print(f"generating answer for {question}")
    if len(question) < 10:
        await update.message.reply_text("question is too short")
        return
    answer = ask_question_from_llm(question)
    await update.message.reply_text(answer)


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "hi back"
    return "nah"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")


if __name__ == "__main__":
    print("Starting bot")
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("ask_question", ask_question))

    # messages
    # app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Polling")
    app.run_polling(poll_interval=3)
