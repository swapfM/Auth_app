from enum import unique
from flask_login import UserMixin
from . import db
   


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(1000), unique = True)
    password = db.Column(db.String(100))
    number = db.Column(db.Integer, default = -1)
    