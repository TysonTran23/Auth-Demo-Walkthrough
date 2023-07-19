from flask import Flask, flash, redirect, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
# from flask_bcrypt import Bcrypt

from models import User, connect_db, db

# from forms import UserForm, TweetForm
# from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
# bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///auth_demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


connect_db(app)
# db.create_all()

toolbar = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("index.html")
