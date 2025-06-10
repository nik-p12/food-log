from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import Meal
from datetime import date
from .generic_resource import GenericResource
from datetime import datetime
meal_field = {
    'id': fields.Integer, 
    'name': fields.String, 
    'date': fields.String,
    'user_id': fields.Integer
    }
meal_parser = reqparse.RequestParser()
meal_parser.add_argument('name', type=str)
meal_parser.add_argument('date', type=str)
meal_parser.add_argument('user_id', type=int)

class MealResource(Resource):
    @marshal_with(meal_field)
    def get(self,id = None):
        if id:
            return Meal.query.get_or_404(id)
        else:
            return Meal.query.all()
        
    @marshal_with(meal_field)
    def post(self):
        args = meal_parser.parse_args()
        meal = Meal(name = args['name'], date = datetime.strptime(args['date'], "%Y-%m-%d %H:%M:%S.%f"), user_id = args['user_id'])
        db.session.add(meal)
        db.session.commit()
        meals = Meal.query.all()
        return meals, 201
    
    @marshal_with(meal_field)
    def patch(self,id):
        args = meal_parser.parse_args()
        meal = Meal.query.filter_by(id = id).first()
        if not meal:
            return 404, "Meal not found"
        if args['name']:
            meal.name = args['name']
        if args['date']:
            meal.date = date = datetime.strptime(args['date'], "%Y-%m-%d %H:%M:%S.%f")
        if args['user_id']:
            meal.user_id = args['user_id']
        db.session.commit()
        return meal
    
    @marshal_with(meal_field)
    def delete(self,id):
        meal = Meal.query.filter_by(id = id).first()
        if not meal:
            abort(404, message = 'meal not found')
        db.session.delete(meal)
        db.session.commit()
        return '', 204

