import datetime as dt
import pprint
import time
import requests
import json
print(dt.datetime.utcnow())
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL)
dict_json = json.loads(response.text)
#pprint.pprint(dict_json)

while True:
    start = dt.datetime.utcnow()
    res = f" курс на {start.strftime('%H:%M:%S')} равен {dict_json['Valute']['EUR']['Value']}"
    print(res)
    time.sleep(5)
