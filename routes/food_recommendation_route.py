from flask_restful import Resource, marshal_with, fields
from services.food_recommendation import recommend_food
food_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'calories': fields.Float,
    'description': fields.String,
}

class FoodRecommendationResource(Resource):
    @marshal_with(food_fields)
    def get(self, user_id):
        foods = recommend_food(user_id)
        return foods
