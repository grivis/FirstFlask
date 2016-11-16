from flask import Flask
from flask import url_for, render_template, request, redirect
from time import *
import pickle

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
        #print(name, lastname, age, sex, residence, language)
        f = open('form' + mmNow + ddNow + hourNow + minNow, 'wb')
        questdic = {'Name': name, 'Lastname': lastname, 'Age': age, 'Sex': sex,
                    'Residence':residence, 'Language':language, 'Coffee':coffeemach,
                    'Television':television, 'Kettle':kettle}
        pickle.dump(questdic, f)
        f.close()
        return render_template('Thanks.html', name=name, birth=age, day=ddNow, month=months[mmNow-1])
    return render_template('NameThings.html')

@app.route('/stats')
def stats():
    import glob, os
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



if __name__ == '__main__':
    app.run(debug=True)