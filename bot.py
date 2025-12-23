import os
from telegram import Bot

TOKEN = os.getenv("8527974239:AAGIgkF6qoyA77X9Elw_LgZZcGT4ncFMEVQ")
CHAT_ID = os.getenv("5355842329")

bot = Bot(token=TOKEN)

async def send_message(text):
    await bot.send_message(chat_id=CHAT_ID, text=text)
