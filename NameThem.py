from flask import Flask
from flask import url_for, render_template, request, redirect
from time import *
import pickle
import glob, os

app = Flask(__name__)


@app.route('/')
def form():
    # Дата и время для регистрации анкеты
    ticks = time()
    lt = localtime(ticks)
    ddNow = str(lt.tm_mday)
    mmNow = str(lt.tm_mon)
    yyyyNow = str(lt.tm_year)
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
        #print(name, lastname, age, sex, residence, language)
        f = open('form' + mmNow + ddNow + hourNow + minNow, 'wb')
        questdic = {'Name': name, 'Lastname': lastname, 'Age': age, 'Sex': sex,
                    'Residence':residence, 'Language':language, 'Coffee':coffeemach,
                    'Television':television, 'Kettle':kettle, 'Iron':iron, 'Smartphone':smartphone}
        pickle.dump(questdic, f)
        f.close()
        return render_template('Thanks.html', name=name, birth=age, day=ddNow, month=months[mmNow-1])
    return render_template('NameThings.html')

@app.route('/stats')
def stats():
    ticks = time()
    lt = localtime(ticks)
    hourNow = str(lt.tm_hour)
    minNow = str(lt.tm_min)
    os.chdir("./")
    count = 0
    cmales = 0
    cfemales = 0
    ccity = 0
    cvillage = 0
    for file in glob.glob("form*"):
        count = count + 1
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
    # HTML текст, который надо выводить в браузер
    ResultText =   '''
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
    ResultTextEnd = '''
</table>
<p>Благодарим за использование нашего сервиса!</p>
</body>
</html>
    '''


    if request.args:
        # Выбор пользователя

        searchword = request.args['SearchWord']
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


        return ResultText + resultstring + ResultTextEnd
    return render_template('Search.html')



if __name__ == '__main__':
    app.run(debug=True)
