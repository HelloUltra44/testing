import telebot
import requests

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['upload'])
def upload_torrent_links(message):
    torrent_link = message.text.split('/upload')[1].strip()
    res = requests.get(torrent_link)
    bot.send_video(message.chat.id, res.content)

bot.polling()
