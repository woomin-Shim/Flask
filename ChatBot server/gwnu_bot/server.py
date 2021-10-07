import os
import urllib

from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, make_response, json   #call module
app = Flask(__name__)


@app.route('/webhook', methods=['GET', 'POST'])  #GET:read Resource, POST:make Resource
def webhook():
    req = request.get_json(force=True)   #Call JSON from Dialogflow
    action = req['queryResult']['action']

    if action == 'Weather':   #Dialogflow에서의 Action value
        name = req['queryResult']['parameters']['geo-city']
        location = name
        url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
        url = url + urllib.parse.quote_plus(location +"날씨")
        soup = BeautifulSoup(urllib.request.urlopen(url).read(),"html.parser")
        temp = soup.findAll("span","todaytemp")
        desc = soup.findAll("p", "cast_txt")

        return {
            "fulfillmentText": location + "의 현재온도는 " + temp[0].text + "도 입니다!!" + "\n"
                               + desc[0].text + "\n"
        }

    elif action == 'Building':
        queryText = req['queryResult']['queryText']

        if "정문" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                            "title": "W1",
                            "subtitle": "W1 picture",
                            "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635074063100.tmp",
                            "buttons": [
                                {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635074063100.tmp"
                                }
                            ]
                        }
                    }
                ]
            }

        elif "w2" in queryText or "보건 건물" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                            "title": "W2",
                            "subtitle": "W2 picture",
                            "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635186229100.tmp",
                            "buttons": [
                                {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635186229100.tmp"
                                }
                            ]
                        }
                    }
                ]
            }

        elif "대학본부" in queryText or "w3" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                            "title": "W3",
                            "subtitle": "W3 picture",
                            "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635248193100.tmp",
                            "buttons": [
                                {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635248193100.tmp"
                                }
                            ]
                        }
                    }
                ]
            }

        elif "w5" in queryText in queryText:
            return {
                "fulfillmentMessages": [
                    {
                        "card": {
                            "title": "W5",
                            "subtitle": "W5 picture",
                            "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635432211100.tmp",
                            "buttons": [
                                {
                                    "text": "크게 보기",
                                    "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635432211100.tmp"
                                }
                            ]
                        }
                    }
                ]
            }

        elif "w6" in queryText or "컴퓨터공학과 건물" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W6",
                        "subtitle": "w6 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635523665100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635523665100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "w7" in queryText or "학생휴게실" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W7",
                        "subtitle": "w7 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635557351100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635557351100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "w8" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W8",
                        "subtitle": "w8 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635373883100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509635373883100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "w11" in queryText or "학식" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W11",
                        "subtitle": "w11 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1540284769316100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1540284769316100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "w12" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W12",
                        "subtitle": "w12 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636040187100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636040187100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "w14" in queryText or "예솔관" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W14",
                        "subtitle": "w14 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636123842100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636123842100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "w15" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "W15",
                        "subtitle": "w15 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636176464100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636176464100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

        elif "청송관" in queryText :
            return {
                "fulfillmentMessages" : [
                    {
                        "card": {
                        "title": "Dormitory",
                        "subtitle": "w15 picture",
                        "imageUri": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636599267100.tmp",
                        "buttons": [
                            {
                                "text": "크게 보기",
                                "postback": "https://www.gwnu.ac.kr/sites/kor/atchmnfl/imgMap/2/temp_1509636599267100.tmp"
                            }
                        ]
                     }
                  }
                ]
            }

    else :
        return "from Webhook"




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


