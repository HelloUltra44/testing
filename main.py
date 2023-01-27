import os
import speedtest
import telegram
from telegram.ext import Updater, CommandHandler

def test(update, context):
    st = speedtest.Speedtest()
    download = st.download()
    upload = st.upload()
    ping = st.results.ping
    update.message.reply_text(f"Download: {download} \nUpload: {upload} \nPing: {ping}")

# token from botfather
TOKEN="5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0"

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('test', test)
dispatcher.add_handler(start_handler)

updater.start_polling()
