import datetime as dt
import requests
import json

print(dt.datetime.utcnow())
URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(URL)
dict_json = json.loads(response.text)



def valute(val):
    if True:
        start = dt.datetime.utcnow()
        res = f"курс на {start.strftime('%H:%M:%S')} равен {dict_json['Valute'][val.upper()]['Value']}"
        return res


x = valute('usd')
print(x)
