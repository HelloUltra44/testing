import speedtest
import telegram
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def test_server_speed(bot, update):
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    update.message.reply_text("Download: %s \nUpload: %s \nPing: %s" % (res['download'], res['upload'], res['ping']))

def main():
    TOKEN = '5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0'
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("test_server_speed", test_server_speed))

    updater.start_polling()
    updater.idle()
