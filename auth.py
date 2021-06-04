from flask import Blueprint
from werkzeug.exceptions import RequestEntityTooLarge
from . import db
from flask import Blueprint, render_template,flash,redirect,url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user
from flask_login import login_user, logout_user, login_required
import random


auth = Blueprint('auth', __name__)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    name = request.form.get('name')
    password = request.form.get('password')


    user = User.query.filter_by(name = name).first()

    if user:
        flash('User already Exists !!')
        return redirect(url_for('auth.signup'))

   
   # a = random.randint(0,99999)
    new_user = User(name = name, password = generate_password_hash(password, method='sha256'))


    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    name = request.form.get('name')
    password = request.form.get('password')
    remember = True if request.form.get('remember')else False

    user = User.query.filter_by(name = name).first()

    if not user or not check_password_hash(user.password, password):
        flash('Invalid Credentials')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
    


