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


def valute(val):
    if val.apper() in dict_json:
        start = dt.datetime.utcnow()
        res = f"курс на {start.strftime('%H:%M:%S')} равен {dict_json['Valute'][val]['Value']}"
        return res
    else:
        return 'none'
x = valute(input())
print(x)