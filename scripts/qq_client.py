from king_chat import Client

client = Client(name="qq", ip="182.254.242.181", port=5920)
client.start(wait=False)


from cqhttp import CQHttp

bot = CQHttp(api_root='http://127.0.0.1:5700/')

@bot.on_message()
def handle_msg(context):
    client.send(context['message'])

    bot.send(context, '你好呀，下面一条是你刚刚发的：')
    return {'reply': context['message'], 'at_sender': False}

bot.run(host='0.0.0.0', port=8080)
