from database.db import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete ="CASCADE"))

    foods = db.relationship('MealFood', cascade="all, delete-orphan", backref='meal', lazy=True)
    health_reactions = db.relationship('HealthReaction', cascade="all, delete-orphan", backref='meal', lazy=True)
