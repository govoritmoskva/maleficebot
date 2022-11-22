"""from random import randint
coin = randint(1,2)
if coin == 1:
    print("Орёл")
if coin == 2:
    print("Решка")"""

import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
USD = (data['Valute']['USD']['Value'])
EUR = (data['Valute']['EUR']['Value'])
KZT = (data['Valute']['KZT']['Value'])
print(USD, EUR, KZT)