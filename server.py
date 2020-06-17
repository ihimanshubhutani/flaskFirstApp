from flask import Flask, render_template, request
from routes import login, signup

app = Flask(__name__, template_folder='views')
app.register_blueprint(login.login, url_prefix="/login")
app.register_blueprint(signup.signup, url_prefix="/signup")


@app.route('/')
def show_index():
    return render_template('index.html', name='himanshu')


app.run(debug=True, host='localhost', port=3000)
