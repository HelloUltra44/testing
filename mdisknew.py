import telebot
from telebot import types
from pySmartDL import SmartDL
import time


token = 'TOKEN'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="send me link", callback_data="url")
    keyboard.add(url_button)  # add button to the keyboard

    bot.send_message(m.chat.id, "Welcome", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)  # check all incoming callbacks for this handler...
def callback_inline(call):  # ...and if it matches the pattern above, handle it with this function!

    if call.data == "url":  # if user clicked on button1... (we set its data="btn1")

        bot.send_message(call.message.chat.id, "Please send me your link")  # answer in the chat and wait for a message from a user (which will be handled by another handler below)

        bot.register_next_step_handler(call.message, getlink)  # and pass the message to another handler which will wait for a user's response with a link (see below)

    else:  # in case of any other data value or lack of it... do nothing at all! :)

        pass


def getlink(m):   # this is where we handle the next step after our button was pressed and we got a message from the user with a link in it! :D

    try:   # try to download file using pySmartDL library (check out README for more info!)

        dlObj = SmartDL(m, progress_bar=False)   # create object of pySmartDL class passing download URL as an argument to constructor... I'm not passing destination path so default temp dir will be used as destination path - you can change that by passing `dest` kwarg to constructor like that: `dlObj = SmartDL('http://example-of-download-link/file', dest='/path/to/destination/folder')` - see README for more info about arguments passed to constructor and available methods of pySmartDL class! :)

        dlObj.start()   # start downloading file using .start() method of created object! :) easy peasy lemon squeezy! :D - check out README for more info about available methods of pySmartDL class! :)    

        fname = dlObj._filename   # getting filename from private property _filename after successful download (this is why I said earlier that you don't need to pass destination path when creating object of pySmartDL class!) - see README for more info about available properties and methods of pySmartDL class! :)    

        msg = open('{}'.format(fname), 'rb')   # opening downloaded file as binary stream so we can send it to Telegram by calling method .sendDocument() on our Bot instance later on in this script... check out README for more info about sending files via Telegram Bot API! :)    

        bot.reply_to(m, "File has been successfully downloaded!")   # just reply back confirming successfull download and saying that file is being sent now...    

        bot.sendDocument(m, msg)   # finally send document using .sendDocument() method on our Bot instance passing ID of chat where we want to upload document as first argument and binary stream containing file itself as second argument (as required by Telegram Bot API)! ;) - check out README for more info about sending files via Telegram Bot API! :)    

    except Exception as e:   # something went wrong while trying to download or upload file? maybe connection error?     print("Exception occured while trying to process request:\n\n{}".format((e)))   return False         return True         @botif __name__ == '__main__':while True:try:print("Listening...")botrun()except KeyboardInterrupt:exit()except Exception as e:print("Exception occured while trying running main loop:\n\n{}".format((e)))time.(5 * 60))</code>enter image description hereenter image description here
