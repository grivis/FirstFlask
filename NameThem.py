'''
Программа реализует лексико-типологическую анкету. Пользователю
демонстрируются изображения предметов, он вводит названия на своем языке
Дополнительно к программе необходимы HTML файлы в папке templates
NameThings.html Thanks.html Search.html Stats.html
a также изображения из папки static
static/coffee.png static/Colorful-Welcome-Text-Header-Image.png
static/iron.png static/kettle.png static/smartphone.png
static/television.png static/thankyou-final-VCH-650x280-600x280.png
Реализованы страницы:
<hostname:port>/ - сама анкета
<hostname:port>/stats - статистика по анкетам
<hostname:port>/search - поиск по анкетам и результаты поиска
<hostname:port>/json - вывод данных всех анкет в формате JSON
'''

# Импортируем нужные модули
from flask import Flask
from flask import render_template, request
from time import *
import pickle
import glob, os
import json

app = Flask(__name__)


@app.route('/')
def form():
    # Дата и время для регистрации анкеты
    ticks = time()
    lt = localtime(ticks)
    ddNow = str(lt.tm_mday)
    mmNow = str(lt.tm_mon)
    hourNow = str(lt.tm_hour)
    minNow = str(lt.tm_min)
    months = ['января', 'февраля', 'марта','апреля','мая',
              'июня','июля','августа','сентября','октября','ноября','декабря']

    if request.args:
        # Анкета
        name = request.args['name']
        lastname = request.args['lastname']
        age = request.args['age']
        sex = request.args['Sex']
        residence = request.args['residence']
        language = request.args['language']
        # Теперь слова
        coffeemach = request.args['coffeemach']
        television = request.args["television"]
        kettle = request.args["kettle"]
        iron = request.args["iron"]
        smartphone = request.args["smartphone"]
        f = open('form' + mmNow + ddNow + hourNow + minNow, 'wb')
        questdic = {'Name': name, 'Lastname': lastname, 'Age': age, 'Sex': sex,
                    'Residence':residence, 'Language':language, 'Coffee':coffeemach,
                    'Television':television, 'Kettle':kettle, 'Iron':iron, 'Smartphone':smartphone}
        pickle.dump(questdic, f)
        f.close()
        return render_template('Thanks.html', name=name, birth=age, day=ddNow, month=months[int(mmNow)-1])
    return render_template('NameThings.html')

@app.route('/stats')
def stats():
    # Выводится статистика по заполненным анкетам
    ticks = time()
    lt = localtime(ticks)
    hourNow = str(lt.tm_hour)
    minNow = str(lt.tm_min)
    os.chdir("./")
    count, cmales, cfemales, ccity, cvillage = 0, 0, 0, 0, 0
    for file in glob.glob("form*"):
        count += 1
        f = open(file, 'rb')
        dic = pickle.load(f)
        if dic['Sex'] == 'male':
            cmales += 1
        else:
            cfemales += 1
        if dic['Residence'] == 'city':
            ccity += 1
        else:
            cvillage += 1
        f.close()

    return render_template('Stats.html', count=count, cmales=cmales, cfemales=cfemales, ccity=ccity,
                           cvillage=cvillage, hour=hourNow, minute=minNow)

@app.route('/search')
def searchform():
    # Пользователь выбирает картинку с предметом и
    #  получает его названия на разных языках
    # HTML текст, который надо выводить в браузер
    ResultHTML =   '''
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Результаты поиска</title>
        <style>
        table, th, td {
        border: 2px solid darkgreen;
        border-collapse: collapse;}
        th, td {
        padding: 15px;}
    </style>
    </head>
    <body style="font-family:Arial;">
    <h1 style="color:darkgreen">Названия предмета, который Вы выбрали:</h1>

    <p></p>
    <table style="width:80%">
      <tr>
        <th>Респондент</th>
        <th>Возраст</th>
        <th>Язык</th>
        <th>Название предмета</th>
      </tr>
    '''
    # Окончание HTML текста
    ResultHTMLEnd = '''
    </table>
    <p>Благодарим за использование нашего сервиса!</p>
    </body>
    </html>
        '''


    if request.args:
        # Выбор пользователя
        searchword = request.args['SearchWord']
        # Обход имеющихся анкет
        os.chdir("./")
        resultstring = ''
        for file in glob.glob("form*"):
            f = open(file, 'rb')
            dic = pickle.load(f)
            word = dic.get(searchword, '---')
            language = dic.get('Language', '---')
            responder = dic.get('Name', '---')
            age = dic.get('Age', '---')
            resultstring += '<tr>'+'<td>'+responder+'</td>'+'<td>'+age+'</td>' \
                             +'<td>'+language+'<td>'+word+'</td>'+'</tr>'+'\n '
            f.close()

        # Выдаем результат в виде HTML документа, в который вставлена таблица результатов поиска
        # Шаблон HTML не сохраняем заранее в виде файла, формируем страницу на лету
        return ResultHTML + resultstring + ResultHTMLEnd
    # вновь возвращаем исходную форму, если не выбран предмет поиска
    return render_template('Search.html')

@app.route('/json')
def jsonout():
    # Вывод всех заполненных анкет в формате HTML
    os.chdir("./")
    alldicts = {}
    for file in glob.glob("form*"):
        f = open(file, 'rb')
        alldicts[file] = pickle.load(f)
        f.close()
    json_string = json.dumps(alldicts)
    return json_string


if __name__ == '__main__':
    app.run(debug=True)
