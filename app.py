from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import User, Food, Meal, MealFood, Category, Allergy, HealthIssue, HealthReaction
from datetime import date
from functools import partial 
from routes import UserResource, category_route, MealResource, MealFoodResource, FoodResource, CategoryResource, AllergyResource, HealthIssueResource, HealthReactionResource, FoodRecommendationResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
api = Api(app)

api.add_resource(UserResource, '/api/users', '/api/users/<int:id>')
api.add_resource(MealResource, '/api/meals', '/api/meals/<int:id>')
api.add_resource(CategoryResource, '/api/categories', '/api/categories/<int:id>')
api.add_resource(MealFoodResource, '/api/meal_foods', '/api/meal_foods/<int:id>')
api.add_resource(HealthIssueResource, '/api/health_issues', '/api/health_issues/<int:id>')
api.add_resource(HealthReactionResource, '/api/health_reactions', '/api/health_reactions/<int:id>')
api.add_resource(AllergyResource,'/api/allergies', '/api/allergies/<int:id>')
api.add_resource(FoodResource, '/api/foods', '/api/foods/<int:id>')

api.add_resource(FoodRecommendationResource, '/users/<int:user_id>/recommendations')

@app.route('/')
def home():
    return render_template("index.html")
    #return "<h1>Practice InF222</h1>"



import random
def populate():
    # Nettoyer les anciennes données
    db.drop_all()
    db.create_all()

    # Création des catégories
    cat_veg = Category(name="Légumes")
    cat_protein = Category(name="Protéines")
    cat_grain = Category(name="Céréales")
    db.session.add_all([cat_veg, cat_protein, cat_grain])
    db.session.commit()

    # Création des aliments
    food1 = Food(name="Carotte", category_id=cat_veg.id)
    food2 = Food(name="Poulet", category_id=cat_protein.id)
    food3 = Food(name="Riz complet", category_id=cat_grain.id)

    db.session.add_all([food1, food2, food3])
    db.session.commit()

    # Création de 5 utilisateurs
    users = []
    for i in range(1, 6):
        user = User(name=f"User {i}", email=f"user{i}@mail.com")
        db.session.add(user)
        users.append(user)
    db.session.commit()

    # Ajout de quelques allergies et problèmes de santé
    allergy1 = Allergy(name="Pollen", description="Réaction au pollen", user_id=users[0].id)
    allergy2 = Allergy(name="Gluten", description="Intolérance au gluten", user_id=users[1].id)
    issue1 = HealthIssue(name="Diabète", description="Type 1", diagnosed_by="Dr House",
                         date_diagnosed=date(2022, 4, 10), user_id=users[0].id)
    issue2 = HealthIssue(name="Hypertension", description="Chronique", diagnosed_by="Dr Strange",
                         date_diagnosed=date(2021, 1, 5), user_id=users[2].id)
    db.session.add_all([allergy1, allergy2, issue1, issue2])
    db.session.commit()

    # Création de repas + associations avec des aliments
    for user in users:
        meal = Meal(name="Déjeuner sain", date=date.today(), user=user)
        db.session.add(meal)
        db.session.commit()

        mf1 = MealFood(meal=meal, food=food1, quantity=100)
        mf2 = MealFood(meal=meal, food=food2, quantity=150)
        db.session.add_all([mf1, mf2])

        # Ajouter une réaction de santé aléatoire pour 2 utilisateurs
        if user.id % 2 == 0:
            reaction = HealthReaction(
                symptom="Maux de ventre",
                severity=2,
                delay_after_meal=1.5,
                notes="Sensation désagréable après le repas",
                date_reported=date.today(),
                user_id=user.id,
                meal_id=meal.id
            )
            db.session.add(reaction)

    db.session.commit()
    print("✅ Base de données peuplée avec succès.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        #populate()
    app.run(debug=True)
