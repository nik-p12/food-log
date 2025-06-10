from database.db import db
from datetime import datetime

class HealthReaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    symptom = db.Column(db.String(255), nullable=False)
    severity = db.Column(db.Integer)  # Ex: 1 (léger) à 5 (grave)
    delay_after_meal = db.Column(db.Float)  # Heures après le repas
    notes = db.Column(db.Text)
    date_reported = db.Column(db.DateTime, default=datetime.utcnow)
