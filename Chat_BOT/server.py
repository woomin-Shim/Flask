from flask import Flask, request, jsonify, make_response, json   #call module
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask'

#def results():
   # data = request.get_json(force=True)   # HTTP 요청의 body에서 json 데이터를 불러옴 --> Open API 호출하고 구현해야 함!
    action = data.get('queryResult').get('action')
    #return {'fullfillmentText' : 'This is a response from webhook'}

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(force=True)
    action = req['queryResult']['action']
    if action == 'Weather':
        name = req['queryResult']['parameters']['person']

    else :
        return "from Webhook"

    return{'fullfillmentText' : name}


@app.route('/static_reply', methods=['POST'])
def static_reply():
    speech = "Hello there, it is from webhook"
    my_result = {
        "speech" : speech,
        "displayText" : speech,
        "source": "apiai-weather-webhook-sample"
    }
    res = json.dumps(my_result, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    app.run(host="localhost", port=5000)