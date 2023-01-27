import telebot
import speedtest

token = '5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! I can test your server speed. Just type /test')

@bot.message_handler(commands=['test'])
def test_message(message):
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    res = st.results.dict()
    bot.send_message(message.chat.id, 'Download speed: {} \nUpload speed: {}'.format(res['download'], res['upload']))

bot.polling()
