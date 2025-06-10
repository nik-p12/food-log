from models import User, Food, HealthIssue, Allergy, HealthReaction
from database.db import db
from sqlalchemy.orm import joinedload

def recommend_food(user_id):
    user = User.query.options(
        joinedload(User.allergies),
        joinedload(User.health_issues),
        joinedload(User.health_reactions)
    ).get(user_id)

    if not user:
        return {"error": "Utilisateur introuvable"}, 404

    # Collecte des aliments associés à des mauvaises réactions
    bad_food_ids = {
        reaction.meal.food_id
        for reaction in user.health_reactions
        if reaction.severity >= 3  # On suppose que 3 et plus est grave
    }

    # Collecte des allergies connues
    allergies = {a.name.lower() for a in user.allergies}

    # Collecte des problèmes de santé (peuvent être utilisés pour filtrer selon des mots-clés par exemple)
    health_issues = {h.name.lower() for h in user.health_issues}

    # Récupère tous les aliments
    all_foods = Food.query.all()
    recommended = []

    for food in all_foods:
        food_name = food.name.lower()

        # Exclusion si aliment dans une allergie connue
        if any(allergen in food_name for allergen in allergies):
            continue

        # Exclusion si aliment a déjà causé une réaction grave
        if food.id in bad_food_ids:
            continue

        # Bonus : exemple simplifié pour des cas de santé
        # (par exemple : éviter le sucre pour le diabète)
        if "diabète" in health_issues and "sucre" in food_name:
            continue

        # Si l’aliment passe tous les filtres
        recommended.append(food)

    return recommended
