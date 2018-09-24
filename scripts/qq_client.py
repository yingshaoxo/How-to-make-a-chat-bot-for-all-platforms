from cqhttp import CQHttp

bot = CQHttp(
    api_root='http://127.0.0.1:5700/'
)


@bot.on_message()
def handle_msg(context):
    bot.send(context, '你好呀，下面一条是你刚刚发的：')
    return {'reply': context['message'], 'at_sender': False}


bot.run(host='0.0.0.0', port=8080)
