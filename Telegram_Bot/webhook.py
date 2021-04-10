import requests
from config import config

config = config() #instance 생성

response = requests.get(config.set_WEBHOOK)  #GET 방식으로 요청
print(response)
