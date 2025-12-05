import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Telegram Bot Token
TOKEN = "8023463275:AAEvNrbcVzz1sG1sacHKYp4YWLQLI1iVNJw"

# Logging ayarları
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    update.message.reply_text("Sinyal botu çalışıyor!")

def handle_signal(update, context):
    message = update.message.text
    update.message.reply_text(f"📩 Sinyal alındı: {message}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_signal))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
