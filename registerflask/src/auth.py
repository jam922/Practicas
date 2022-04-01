from flask import Blueprint
from . import db

auth = Blueprint('entorno_virtual', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/usuarios')
def usuarios():
    return 'usuarios'