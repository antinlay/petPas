from xmlrpc.client import boolean
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine, desc

Base = declarative_base()

engine = create_engine('sqlite:///test.db', echo=True)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    telegram_username = db.Column(db.String(80), unique=True, nullable=False)
    platform_username = db.Column(db.String(80), unique=True, nullable=False)
    city_id = db.Column(db.Integer, ForeignKey("city.city_id"), nullable=False)
    wave_id = db.Column(db.Integer, ForeignKey("wave.wave_id"), nullable=False)
    tribe_id = db.Column(db.Integer, ForeignKey("tribe.tribe_id"), nullable=False)
    admin_status = db.Column(db.Boolean, nullable=False)
    user_answers = relationship("User_answer")

    def __repr__(self):
        return '<User %r>' % self.user_id


class Wave(db.Model):
    wave_id = db.Column(db.Integer, primary_key=True)
    wave_number = db.Column(db.String(80), unique=True, nullable=False)
    users = relationship("User")

    def __repr__(self):
        return '<Wave %r>' % self.wave_number

class Tribe(db.Model):
    tribe_id = db.Column(db.Integer, primary_key=True)
    tribe_name = db.Column(db.String(80), unique=True, nullable=False)
    users = relationship("User")

    def __repr__(self):
        return '<Tribe %r>' % self.tribe_name

class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(80), unique=True, nullable=False)
    users = relationship("User")

    def __repr__(self):
        return '<City %r>' % self.city_name


class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(300), nullable=False)
    question_status = db.Column(db.Boolean, nullable=False)
    question_public_status = db.Column(db.Boolean, nullable=False)
    answers = relationship("Answer")

    def __repr__(self):
        return '<Question %r>' % self.question_text

    def __init__(self, question_id, question_text, question_status, question_public_status):
        self.question_id = question_id
        self.question_text = question_text
        self.question_status = question_status
        self.question_public_status = question_public_status


class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String(300), nullable=False)
    question_id = db.Column(db.Integer, ForeignKey(
        "question.question_id"), nullable=False)
    user_answers = relationship("User_answer")

    def __repr__(self):
        return '<Answer %r>' % self.answer_text

    def __init__(self, question_id, answer_text):
        self.answer_text = answer_text
        self.question_id = question_id


class User_answer(db.Model):
    user_answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    answer_id = db.Column(db.Integer, ForeignKey(
        "answer.answer_id"), nullable=False)
    question_id = db.Column(db.Integer, ForeignKey(
        "question.question_id"), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey(
        "user.user_id"), nullable=False)

    def __repr__(self):
        return '<user_answer_id %r>' % self.user_answer_id