from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    team = db.Column(db.String(50))
    role = db.Column(db.String(10)) # WK, BAT, AR, BOWL
    credits = db.Column(db.Float)
    points_predicted = db.Column(db.Float, default=0.0)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team1 = db.Column(db.String(50))
    team2 = db.Column(db.String(50))
    match_date = db.Column(db.String(50))
