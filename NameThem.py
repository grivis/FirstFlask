from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def form():
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
        print(name, lastname, age, sex, residence, language)
        return render_template('aform.html', name=name, birth=age)
    return render_template('NameThings.html')


if __name__ == '__main__':
    app.run(debug=True)