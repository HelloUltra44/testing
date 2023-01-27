import speedtest
import telegram
from telegram.ext import Updater, CommandHandler

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello! I am here to help you test your server's speed")

def test_speed(bot, update):
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    result = s.results.dict()
    bot.send_message(chat_id=update.message.chat_id, text=f"Your download speed is {result['download']} and your upload speed is {result['upload']}")

def main():
    bot = telegram.Bot(token="5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0")
    updater = Updater(bot.token)
    start_handler = CommandHandler('start', start)
    speed_handler = CommandHandler('test_speed', test_speed)
    updater.dispatcher.add_handler(start_handler)
