class config():  #class안에서 변수들을 관리
    def __init__(self):
        # token이 필요하기 때문에 저장
        self.API_KEY = "1750148053:AAG4fHbiajhZCkUmGN1CYx0Zvgy14wjjnGg"
        # webhook을 걸때 ngrok으로 포워딩 시킨 주소를 보내주어야 정상적으로 작동
        self.WEBHOOK_URL = "https://2ff6fb50d8ce.ngrok.io"  #local host를 포워딩시킨 주소

        # 실제로 webhook을 걸어준다
        # 요청을 보내주는 방식은 query, json 등이 있음, 현재는 query방식
        self.set_WEBHOOK = "https://api.telegram.org/bot{API_KEY}/setWebhook?url={WEBHOOK_URL}"\
        .format(API_KEY=self.API_KEY,WEBHOOK_URL=self.WEBHOOK_URL) #formating

        # API --> send_message
        self.send_message = "https://api.telegram.org/bot{API_KEY}/sendMessage"\
        .format(API_KEY=self.API_KEY, )
