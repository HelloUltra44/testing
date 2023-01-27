import logging

from telegram.ext import Updater, CommandHandler
import speedtest

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi! I\'m a bot to test your server speed from speedtest.net.\n\n'
                              'Type /test to start a speed test.')


def test(update, context):
    st = speedtest.Speedtest()
    download = st.download()
    upload = st.upload()
    ping = st.results.ping
    update.message.reply_text('Your server speed is:\n\n'
                              'Download: {:.2f} Mbps\n'
                              'Upload: {:.2f} Mbps\n'
                              'Ping: {:.2f} ms'.format(download/1e6, upload/1e6, ping))


def main():
    # Telegram API token
    updater = Updater('5961186050:AAFLW57la19tvwiwVfHlLKoVWFk_ng0uNj0', use_context=True)

    # Getting dispatcher to register handlers
    dp = updater.dispatcher

    # Adding command handler to dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('test', test))

    # Starting the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if name == '__main__':
    main()
