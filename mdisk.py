
import requests
from telegram.ext import Updater

def send_to_mdisk(file_id):
    # define the mdisk.me api url
    url = 'https://mdisk.me/api/upload/telegram'

    # define the parameters to be sent
    params = {'token': 'your_mdisk_token',
              'file_id': file_id}

    # sending the request and saving the response
    response = requests.post(url, params=params)

    # extract the json response
    response_json = response.json()

    return response_json['link']

# create a bot
updater = Updater(token='your_telegram_token', use_context=True)

# handle the start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Hello! I'm Mdisk Bot. I will help you to upload Telegram files to Mdisk.me")

# handler the upload command
def upload(update, context):
    # get the file_id
    file_id = context.args[0]

    # generate mdisk.me link
    link = send_to_mdisk(file_id)

    # send the link
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f"Here is your Mdisk.me link: {link}")

# add handlers to the bot
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('upload', upload))

# start the bot
updater.start_polling()
