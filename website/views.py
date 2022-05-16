# Stores all the views that the user can navigate to, except the authentication page which is in auth

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"

