from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import MealFood
from datetime import date
from .generic_resource import GenericResource

meal_food_field = {
    'id': fields.Integer, 
    'quantity': fields.Integer, 
    'meal_id': fields.Integer, 
    'food_id': fields.Integer
    }
meal_food_parser = reqparse.RequestParser()
meal_food_parser.add_argument('quantity', type=int)
meal_food_parser.add_argument('meal_id', type=int)
meal_food_parser.add_argument('food_id', type=int)

class MealFoodResource(Resource):
    @marshal_with(meal_food_field)
    def get(self,id = None):
        if id:
            return MealFood.query.get_or_404(id)
        return MealFood.query.all()
    
    @marshal_with(meal_food_field)
    def post(self,id):
        args = meal_food_parser.parse_args()
        mf = MealFood(quantity = args['quantity'], meal_id = args['meal_id'], food_id = args['food_id'])
        db.session.add(mf)
        db.session.commit()
        meal_foods = MealFood.query.all()
        return meal_foods
    
    @marshal_with(meal_food_field)
    def patch(self, id):
        args = meal_food_parser.parse_args()
        meal_food = MealFood.query.filter_by(id = id).first()
        if not meal_food:
            abort(404, message = 'meal food not found')
        if args['quantity']:
            meal_food.quantity = args['quantity']
        if args['meal_id']:
            meal_food.meal_id = args['meal_id']
        if args['food_id']:
            meal_food.food_id = args['food_id']
        db.session.commit()
        return meal_food
    
    @marshal_with(meal_food_field)
    def delete(self, id):
        meal_food = MealFood.query.filter_by(id = id).first()
        if not meal_food:
            abort(404, message= 'meal food not found')
        db.session.delete(meal_food)
        db.session.commit()
        return '',204