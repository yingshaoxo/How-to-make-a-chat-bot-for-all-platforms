# client
from king_chat import Client

client = Client(name="telegram", ip="182.254.242.181", port=5920)

@client.on_received
def on_received(protocol, text):
    print(text)

client.start(wait=False)

while 1:
    text = input('words: ')
    client.send(text)
