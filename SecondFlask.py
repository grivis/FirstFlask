from flask import Flask, render_template

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/<thing>')
def home(thing):
    return render_template('flask2.html', thing=thing)

@app.route('/echo/<thing>')
def echo(thing):
    return thing

app.run(port=7777, debug=True)