from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application import db

class MEALS(db.Model):
    meal_id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20),nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    Reservations = db.relationship('reservations', backref='meals') 

class Tables(db.Model):
    table_no = db.Column(db.Integer, primary_key=True)
    no_of_prople = db.Column(db.Integer, nullable=False)
    time_booked = db.Column(db.timestamp, nullable=False)
    Reservations = db.relationship('resevations', backref='tables')

class Reservations(db.Model):
    reservation_id =id = db.Column(db.Integer, primary_key=True) 
    meal_id= db.Column(db.Integer, db.ForeignKey('meals.id'), nullable=False)
    table_no=db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)

class TodoForm(FlaskForm):
    task = StringField("Task")
    submit = SubmitField("Add Todo")