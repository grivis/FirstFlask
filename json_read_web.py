'''
Скачиваем все анкеты с сайта http://flask.grivis.ru/json и преобразуем обратно в объект Питон
Обращаем внимание, что все нестандартные символы - т.е. все, кроме стандартной латиницы,
представлены в JSON-выводе в виде кодов.
Преобразованию подверглись русские буквы, буквы с диакритикой во французском и польском языках.
В процессе обратного преобразования они были корректно восприняты.
'''
import json
from urllib.request import urlopen

responce = urlopen('http://flask.grivis.ru/json').read().decode('utf-8')

alldict = json.loads(responce)

for onedict in alldict.values():
    for key, value in onedict.items():
        print(key, value)
    print('-------')