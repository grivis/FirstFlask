from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/<thing>')
def home(thing):
    return app.send_static_file('templates/flask2.html')

@app.route('/echo/<thing>')
def echo(thing):
    return thing

app.run(port=7777, debug=True)