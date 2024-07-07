from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash #to hash passwords
from . import db
from flask_login import login_user,login_required,logout_user,current_user

# flash = to flash the messages on the screen

auth=Blueprint('auth',__name__)

# by default it vl b GET requests

# text is a variable passed to login.html page n now it can b accesed in login.html page (can pass multiple variables) ex:{{text + "s"}}-->jinja template lang
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        # checking whether the user exists in the database
        user=User.query.filter_by(email=email).first()#checks for specific field
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully!',category='success')
                login_user(user,remember=True)#stores the session or remembers user
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password,try again!',category='error')
        else:
            flash('Email does not exist.',category='error')
                

    return render_template("login.html",user=current_user)


@auth.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signUp',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email=request.form.get('email') #to get specific value 
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        user=User.query.filter_by(email=email).first()#checks for specific field
        if user:
            flash('Email already exist.',category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName)<2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1!=password2:
            flash('Passwords don\'t match.' ,category='error')
            # don't ,it vl gv error so escape character is used (don\'t)
        elif len(password1)<7:
            flash('Password must be atleast 7 characters.', category='error')
        else:
            # add user to database
            new_user=User(email=email,first_name=firstName,password=generate_password_hash(password1,method='pbkdf2:sha256'))
            # werkzeug.security.generate_password_hash function does not directly support sha256 as a method. Instead, it supports pbkdf2:sha256, which is a more secure way to hash passwords.

            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            login_user(user,remember=True)
            return redirect(url_for('views.home'))
            # return redirect('/)->similar


    return render_template("signUp.html",user=current_user)


# in html file
    # return render_template("login.html",text="Testing",boolean=False)
# 
# <h1>This is the login page</h1>
# {{text}}
# {% if boolean == True %}
# yes it is true!
# 
# {% elif %}

# {% else %}
# No it is not true!
# {% endif %} 