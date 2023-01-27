
import telebot
import speedtest

bot = telebot.TeleBot('5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm Speedtest-bot. I can measure your server speed.")

@bot.message_handler(commands=['speedtest'])
def send_speedtest(message):
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()

    bot.reply_to(message,
    """
    Your download speed is {}
    Your upload speed is {}
    Your ping is {}
    """.format(res['download'], res['upload'], res['ping']))

bot.polling()
