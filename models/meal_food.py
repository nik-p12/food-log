from database.db import db

class MealFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id', ondelete="CASCADE"), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id', ondelete="CASCADE"), nullable=False)
    quantity = db.Column(db.Float, nullable=False)  # par exemple en grammes

