from telegram import Bot
import os

bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

async def send_message(text):
    """Envia uma mensagem para o Telegram."""
    await bot.send_message(chat_id=CHAT_ID, text=text)
