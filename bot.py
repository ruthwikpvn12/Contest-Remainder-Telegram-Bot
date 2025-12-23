import os
from telegram import Bot

TOKEN = os.getenv("8527974239:AAGIgkF6qoyA77X9Elw_LgZZcGT4ncFMEVQ")
CHAT_ID = os.getenv("5355842329")

bot = None

if TOKEN:
    try:
        bot = Bot(token=TOKEN)
    except Exception as e:
        print("Telegram bot init failed:", e)

def send_message(text):
    if not bot or not CHAT_ID:
        print("Bot or CHAT_ID missing. Skipping message.")
        return

    try:
        bot.send_message(chat_id=CHAT_ID, text=text)
    except Exception as e:
        print("Failed to send message:", e)
