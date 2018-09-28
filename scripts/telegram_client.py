from king_chat import Client

client = Client(name="telegram", ip="182.254.242.181", port=5920)


from telegram.ext import Updater

last_user_id = 0
my_bot = None

updater = Updater(token='684605925:AAFtHdx9p2Hi8vzFNC5dFV2qshwKLw0y0lA')
dispatcher = updater.dispatcher

"""
def start_function(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, 
        text="I'm a bot, please talk to me!"
    )
    
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start_function)
dispatcher.add_handler(start_handler)
"""

def echo(bot, update):
    global last_user_id
    global my_bot
    last_user_id = update.message.chat_id
    my_bot = bot

    client.send(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


@client.on_received
def on_received(protocol, text):
    global last_user_id
    global my_bot
    if last_user_id != 0 and my_bot != None: 
        print(text)
        my_bot.send_message(chat_id=last_user_id, text=text)


client.start(wait=False)
updater.start_polling()
