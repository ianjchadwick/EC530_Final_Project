# Stores all the views that the user can navigate to, except the authentication page which is in auth

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

