from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    date = db.Column(db.DateTime(), default=date.today())

class Subcategories(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    subcategory = db.Column(db.String(150), unique=True)
    subdescription = db.Column(db.String(500))
    catid = db.Column(db.Integer, db.ForeignKey('categories.id'))
    username = db.Column(db.String(150))
    date = db.Column(db.DateTime(), default=date.today())

class Categories(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(150), unique=True)
    description = db.Column(db.String(500))
    subcats = db.relationship('Subcategories')
    username = db.Column(db.String(150))
    date = db.Column(db.DateTime(), default=date.today())

class SearchTransactions(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(150))
    date = db.Column(db.DateTime(), default=date.today())