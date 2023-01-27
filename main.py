import speedtest
import telebot

bot_token = 'Your_bot_token'
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello! To test your server speed, type /speedtest')

@bot.message_handler(commands=['speedtest'])
def send_speedtest(message):
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    results_dict = s.results.dict()
    download_speed = results_dict['download']
    upload_speed = results_dict['upload']
    bot.reply_to(message, f'Your download speed is {download_speed} Mbps \nYour upload speed is {upload_speed} Mbps')

bot.polling()
