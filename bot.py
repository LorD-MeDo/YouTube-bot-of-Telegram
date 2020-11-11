
#Download YouTube Videos :- https://medo.gq :- https://t.me/GGGGw
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

import youtube_dl

import random

PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#YOUR TOKEN :
logger = logging.getLogger(__name__)
TOKEN = 'YOUR TOKEN'
def start(update, context):
    print("hi")
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Send me Url YouTube! Or send /Help')
def help(update, context):
    """Send a message when the command /help is issued."""
    #Thes Message a /start :
    update.message.reply_text('@cC14Cc')
    item_yes = InlineKeyboardButton('فهمت!', callback_data='yes')
    markup_reply = InlineKeyboardMarkup([[item_yes]])
    update.message.reply_text('Hi Donkey :-  Go to YouTube and click share, copy the link and send it to me or use the internal bot @vid to search and download videos For example: @vid mala mia If you dont understand contact the developer : @GGGGw', reply_markup=markup_reply)
def callback_query(update, context):
    if update.callback_query.data == 'yes':
        update.callback_query.edit_message_text('Ok Donkey Send Me Url now !')
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
alp = 'qwertyuioplkjhgfdsazxcvbnm'
def echo(update, context):
    if update.message.entities:
        for item in update.message.entities:
            if item.type == "url" and update.message.text.find('  ') == -1:
                if 'youtube.com' in update.message.text or 'youtu.be' in update.message.text:   
                    doc1 = random.choices(alp, k=10)
                    doc = ""
                    for j in doc1:
                        doc+=j
                    doc = '4'
                    if os.path.exists('m.mp4'):
                        os.remove('{}.mp4'.format(doc))
                    else:
                        pass
                    
                    ydl_opts = {'outtmpl': '{}.mp4'.format(doc), 'max_filesize': 600000000000000, 'preferredcodec': 'mp4'}
                    
                    link_of_the_video = update.message.text 
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([link_of_the_video])

                    video = open('{}.mp4'.format(doc), 'rb')
                    update.message.reply_document(video)
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(MessageHandler(Filters.text, echo))

dp.add_handler(CallbackQueryHandler(callback_query))
    
dp.add_error_handler(error)
updater.start_polling()

