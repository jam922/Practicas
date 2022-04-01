from flask import Flask, render_template,request,redirect,url_for,flash,jsonify
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, logout_user
from config import config
import random
from datetime import datetime
#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User
'''import os
SECRET_KEY = os.urandom(32)
'''

app=Flask(__name__)
db=MySQL(app)
login_manager_app = LoginManager(app)
csrf=CSRFProtect()
#app.config['SECRET_KEY'] = SECRET_KEY


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(None,request.form['username'],request.form['password'],None)
        register_user = ModelUser.login(db,user)
        flash("Usuario Registrado!!")
        return redirect(url_for('home'))
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/usuarios', methods=['GET'])
def usuarios():
    try:
        cursor = db.connection.cursor()
        sql = "SELECT id, username, password FROM user"
        cursor.execute(sql)
        db.connection.commit()
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            usuario={'id':fila[0],'username':fila[1],'password':fila[2]}
            usuarios.append(usuario)
        return jsonify({'usuarios':usuarios,'mensaje':"usuarios listados."})
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

def status_401(error):
    return redirect(url_for('login'))        


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404, status_404)
    app.run()