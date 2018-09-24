from telegram.ext import Updater

updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher


def start_function(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, 
        text="I'm a bot, please talk to me!"
    )
    
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start_function)
dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
