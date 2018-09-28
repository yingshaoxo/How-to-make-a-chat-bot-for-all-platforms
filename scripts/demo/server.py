# server
from king_chat import Server

server = Server(ip="127.0.0.1", port=5920)

@server.on_received
def handle(protocol, text):
    print(text)
    protocol.send_to_all_except_sender(text)

server.start(wait=False)
while 1:
    server.send_to_one(name='telegram', text=input('words: '))
