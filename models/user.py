from database.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    meals = db.relationship('Meal', backref='user', lazy=True)
    allergies = db.relationship('Allergy', backref='user', lazy=True)
    health_issues = db.relationship('HealthIssue', backref='user', lazy=True)
    health_reactions = db.relationship('HealthReaction', backref='user', lazy=True)
