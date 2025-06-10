from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import Food
from datetime import date
from .generic_resource import GenericResource

food_field = {
    'id': fields.Integer,
    'name': fields.String
    }
food_parser = reqparse.RequestParser()
food_parser.add_argument('name', type=str, required=True)
food_parser.add_argument('calories', type= float)
food_parser.add_argument('description', type=str)
food_parser.add_argument('category_id', type=int)

class FoodResource(Resource):
    @marshal_with(food_field)
    def get(self, id = None):
        if id:
            return Food.query.get_or_404(id)
        return Food.query.all()
    @marshal_with(food_field)
    def post(self):
        args = food_parser.parse_args()
        food =  Food(name = args['name'], calories = args['calories'], description = args['description'], category_id = args['category_id'])
        db.session.add(food)
        db.session.commit()
        foods = Food.query.all()
        return foods, 201

    @marshal_with(food_field)
    def patch(self,id):
        args = food_parser.parse_args()
        food = Food.query.filter_by(id = id).first()
        if not food:
            return abort(404, message = 'food not found')
        if args['name']:
            food.name = args['name']
        if args['calories']:
            food.calories = args['calories']
        if args['description']:
            food.description = args['calories']
        if args['category_id']:
            food.categories_id = args['category_id']
        db.session.commit()
        return food

    @marshal_with(food_field)
    def delete(self, id):
        food = Food.query.filter_by(id = id).first()
        if not food:
            abort(404, message = 'food not found')
        db.session.delete(food)
        db.session.commit()
        return '', 204