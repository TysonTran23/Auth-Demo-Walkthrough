from flask import Flask, flash, redirect, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserForm
from models import User, connect_db, db

app = Flask(__name__)
# bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///auth_demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.username.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        db.session.commit()
        flash("Welcome! You have successfully created your account")
        return redirect('/tweets')

    return render_template("register.html", form=form)

@app.route('/tweets')
def show_tweets():
    return render_template('tweets.html')

@app.route('/login', methods=["GET", "POST"])
def login_user():
    form = UserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            return redirect('/tweets')
        else:
            form.username.errors = ['Invalid Username/Password']

    return render_template('login.html', form=form)
