from flask import Blueprint
from . import db
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import User
import random

main = Blueprint('main', __name__)


def generate():
    a = random.randint(0,99999)
    print(a)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    generate()
    return render_template('profile.html', name = current_user.name)