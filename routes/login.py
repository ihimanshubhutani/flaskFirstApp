from flask import Blueprint, render_template

# static, template folder path can be defined here
login = Blueprint('login', __name__)


@login.route('/')
def show_login_page():
    return render_template('login.html')
