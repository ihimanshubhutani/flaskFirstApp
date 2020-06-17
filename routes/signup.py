from flask import Blueprint, render_template

# static, template folder path can be defined here
signup = Blueprint('signup', __name__)


@signup.route('/')
def show_signup_page():
    return render_template('signup.html')
