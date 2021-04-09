from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello ChatBot!"

@app.route('/GWNU/<username>', methods=['GET'])
def get_name(username):
    return "name : " + username


@app.route('/message/<int:message_id>')
def get_message(message_id):
    return "message_id : %d" % message_id

if __name__ == "__main__":
        app.run(debug=True, host="localhost", port=5000)
