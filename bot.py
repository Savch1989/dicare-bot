import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(level=logging.INFO)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я DICare-бот. Чем могу помочь?')

def main():
    updater = Updater('7635205082:AAGqq74uxQIFyTJJszlWMmjvODXGT-62jHI')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
