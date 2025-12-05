from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from analysis import technical_analysis
import os

TOKEN = os.getenv("TOKEN")  # Token burada environment olarak okunacak

# /start komutu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Borsa Asistanına Hoşgeldin!\n\n"
        "Hangi sembolü analiz etmemi istersin?\n"
        "Örnek: BTC-USD, BIST:XU100, EURUSD=X"
    )

# Kullanıcı sembol yazınca analiz yap
async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = update.message.text.upper()

    result = technical_analysis(symbol)

    await update.message.reply_text(result, parse_mode="Markdown")

# Botu başlatma fonksiyonu
async def main():
    app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze))

    print("Bot çalışıyor...")
    await app.run_polling()
