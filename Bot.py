from telegram.ext import Updater, CommandHandler

import os
TOKEN = os.getenv("TOKEN")

def Start(update,context):
    update.message.reply_text(" Bot Is Working \n Use /Play To Start The Game ")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

def Play(update,context):
    update.message.reply_text(" Yeah You Can Play !!! ")

dp.add_handler(CommandHandler("start",Start))
dp.add_handler(CommandHandler("Play",Play))

updater.start_polling()
updater.idle()

