from king_chat import Client

client = Client(name="qq", ip="182.254.242.181", port=5920)


from cqhttp import CQHttp

last_context = None
bot = CQHttp(api_root='http://127.0.0.1:5700/')

def filter(text):
    """
    作业 or 交
    页 and 题
    报名 or 缴费
    课 and 上
    面试 or 校招
    """
    if ('作业' in text) or ('交' in text):
        return text
    elif ('页' in text) and ('题' in text):
        return text
    elif ('报名' in text) or ('缴费' in text):
        return text
    elif ('课' in text) and ('上' in text):
        return text
    elif ('面试' in text) or ('校招' in text):
        return text
    return ''

@bot.on_message()
def handle_msg(context):
    global last_context
    last_context = context

    new_text = filter(context['message'])
    if new_text != "":
        client.send(new_text)

    bot.send(context, '你好呀，下面一条是你刚刚发的：')
    return {'reply': context['message'], 'at_sender': False}

@client.on_received
def on_received(protocol, text):
    global last_context
    global bot
    bot.send(last_context, text)


client.start(wait=False)
bot.run(host='0.0.0.0', port=8080)

