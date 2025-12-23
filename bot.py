import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# রেন্ডারে বোট সচল রাখার জন্য সার্ভার
app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"
def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("অভিনন্দন! আপনার বোটটি কাজ করছে।")

if __name__ == '__main__':
    # নিচের লাইনে আপনার আসল টোকেন বসান
    TOKEN = "8309172328:AAEUhXGeR2XtPWz5zA3zTZjj0nzVm2NYlhw"
    keep_alive()
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
