from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://mysql_user:mysql_password>@mysql_instance_ip>:3306/<mysql_db>'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:1234@35.189.79.75:3306/TESTDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
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
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')