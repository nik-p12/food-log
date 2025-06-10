from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import User
from datetime import date
from .generic_resource import GenericResource

user_field = {
    'id': fields.Integer,
    'name': fields.String
    }
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True)
user_parser.add_argument('email', type = str)
class UserResource(Resource):
    @marshal_with(user_field)
    def get(self,id = None):
        if id: 
            return User.query.get_or_404(id)
        else:
            return User.query.all()
        
    @marshal_with(user_field)
    def post(self):
        args = user_parser.parse_args()
        user =  User( name = args['name'], email = args['email'])
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
        return users, 201
    
    @marshal_with(user_field)
    def patch(self,id):
        args = user_parser.parse_args()
        user = User.query.filter_by(id = id).first()
        if not user:
            abort(404, message = "User not found")
        if args['name']:
            user.name = args['name']
        if args['email']:
            user.email = args['email']
        db.session.commit()
        return user

    @marshal_with(user_field)
    def delete(self, id):
        user = User.query.filter_by(id = id).first()
        if not user:
            abort(404, message = 'user not found')
        db.session.delete(user)
        db.session.commit()
        return '', 204