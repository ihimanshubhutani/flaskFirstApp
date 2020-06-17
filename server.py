from flask import Flask, render_template, request

app = Flask(__name__, template_folder='views')


@app.route('/')
def show_index():
    return render_template('index.html', name='himanshu')


@app.route('/login')
def show_login():
    return "hello"


@app.route('/login')
def signin_user():
    return request.body


app.run(debug=True, host='localhost', port=3000)
