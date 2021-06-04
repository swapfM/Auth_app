from flask import Blueprint
from . import db
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User
import random

main = Blueprint('main', __name__)


def generate():
    a = random.randint(0,99999)
    


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name = current_user.name, num = current_user.number)


@main.route('/profile', methods=['POST'])
@login_required
def profile_post():
    a = random.randint(0,99999)
    current_user.number = a
    db.session.commit()
    return render_template('profile.html', name = current_user.name, num = current_user.number)

@main.route('/', methods=['POST'])
@login_required
def index_post():
    return render_template('index.html', num = current_user.number)


