from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)
@auth.route('/', methods=["GET", "POST"])
def home():
    data = request.form
    print(data)

@auth.route('/login', methods= ["GET", "POST"])
def login():
    return render_template("login.html")


@auth.route('/logout', methods=["GET", "POST"])
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")