from flask import Flask, request
from bot import Bot


app = Flask(__name__)

@app.route('/', methods=['POST']) #POST 방식으로 요청을 받음
def hello():
    data = request.get_json()
    print(data)

    bot = Bot()
    bot(data)

    print(bot.chat_id)
    print(bot.name)

    if("강릉원주" in bot.msg) :     #사용자가 보낸 메세지에 강릉원주가 있으면
        bot.sendMessage("강릉원주대 Chatbot 시작합니다")

@app.route('/GWNU/<username>')
def get_name(username):
    #data = request.get_json()
    #print(data)
    return "name : " + username


@app.route('/message/<int:message_id>')
def get_message(message_id):
    return "message_id : %d" % message_id

if __name__ == "__main__":
        app.run(debug=True, host="localhost", port=5000)
