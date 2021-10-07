import requests
from config import config
config = config()

class Bot:
    def __init__(self):
        self.chat_id = None
        self.name = None
        self.msg = None

    #parsing
    def __call__(self, data):
        chat_id = data['message']['chat']['id']
        name = data['message']['chat']['last_name'] + data['message']['chat']['first_name']
        msg = data['message']['text']

        self.chat_id = chat_id
        self.name = name
        self.msg = msg


    def sendMessage(self,text):
        params = {'chat_id' : self.chat_id, 'text' : text}
        requests.post(config.send_message, json=params)