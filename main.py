#importing all the necessary libraries
import json
import requests
import speedtest
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

# function to test speed
def speed_test(bot, update):
    #performing speed test
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()
    results_dict = s.results.dict()
    #storing results in variables
    download = results_dict["download"]
    upload = results_dict["upload"]
    ping = results_dict["ping"]
    #converting results into megabits
    download_mb = download / 1000000
    upload_mb = upload / 1000000
    #output the results
    response = (f'Your speed test results\n'
                f'Download Speed: {download_mb} Mbps\n'
                f'Upload Speed: {upload_mb} Mbps\n'
                f'Ping: {ping} ms\n')
    #send response to the user
    bot.send_message(chat_id=update.message.chat_id, text=response)

# main function
def main():
    #creating telegram bot
    updater = Updater(token = '5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0')
    dispatcher = updater.dispatcher
    #adding handler
    dispatcher.add_handler(CommandHandler('speedtest', speed_test))
    #start the bot
    updater.start_polling()
    #run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
