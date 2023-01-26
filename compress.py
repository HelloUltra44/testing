#importing libraries 
import os
import subprocess

#importing modules
from telegram.ext import Updater, CommandHandler

#connecting to the bot
updater = Updater(token='<your-token>', use_context=True)
dispatcher = updater.dispatcher

#defining function for compress video command
def compress_video(update, context):
    #getting the video file
    file_id = update.message.document.file_id
    file_name = update.message.document.file_name
    path = context.bot.get_file(file_id).file_path
    
    #compressing the video
    output_name = file_name.split('.')[0] + '_compressed.mp4'
    subprocess.call(['ffmpeg', '-i', path, '-vcodec', 'libx264', '-preset', 'slow', '-crf', '22', '-acodec', 'copy', output_name])
    
    #sending the compressed video
    file = open(output_name, 'rb')
    context.bot.send_document(chat_id=update.message.chat_id, document=file)
    
    #removing the compressed video
    os.remove(output_name)

#defining command handler
compress_handler = CommandHandler('compressvideo', compress_video)
dispatcher.add_handler(compress_handler)

#start the bot
updater.start_polling()
