# this file makes a website folder as a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db=SQLAlchemy() #object
DB_NAME="database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='FlaskWebApp'#encrypt or secure the cookies in session data related to the website

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  #tells flsk that sqlite database is stored at that location  # stores at website floder #f string works only in version greater than python6
    
    db.init_app(app) #initializing the database by gvng the flask app

    
    # tells the flask app about the built components for the website
    from .views import views
    from .auth import auth

    # registering with flask application
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/') #prefix is like if url_prefix='/auth/' n app.route('home')->/auth/home

    from .models import User,Note

    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view ='auth.login' #tells where flask should redirect if user is not loggedin
    login_manager.init_app(app) #tells the login manager which app v r using

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        with app.app_context():#makes sure that flask app is active
            db.create_all()#app=app tells to sqlalchemy that ,to vch app vr creating database
            print("Created database!")