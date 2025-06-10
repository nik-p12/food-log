from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import Category
from datetime import date
from .generic_resource import GenericResource

category_field = {
    'id': fields.Integer, 
    'name': fields.String
    }
category_parser = reqparse.RequestParser()
category_parser.add_argument('name', type=str, required=True)

class CategoryResource(Resource):
    @marshal_with(category_field)
    def get(self, id = None):
        if id:
            return Category.query.get_or_404(id)
        return Category.query.all()
    
    @marshal_with(category_field)
    def post(self):
        args =category_parser.parse_args()
        cat = Category(name = args['name'])
        db.session.add(cat)
        db.session.commit()
        categories = Category.query.all()
        return categories,201
    
    @marshal_with(category_field)
    def patch(self, id):
        args = category_parser.parse_args()
        category = Category.query.filter_by(id = id).first()
        if not category:
            abort(404, message = 'category not found')
        category.name = args['name']
        db.session.commit()
        return category
    
    @marshal_with(category_field)
    def delete(self, id):
        category = Category.query.filter_by(id  = id).first()
        if not category:
            abort(404, message = 'category not found')
        db.session.delete(category)
        db.session.commit()
        return '', 204