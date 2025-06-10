from database.db import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Float)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    meal_associations = db.relationship('MealFood', backref='food', lazy=True)
    category = db.relationship('Category', backref='foods')
