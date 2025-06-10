from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import Allergy
from datetime import date
from .generic_resource import GenericResource

allergy_field = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'user_id': fields.Integer
}

allergy_parser = reqparse.RequestParser()
allergy_parser.add_argument('name', type=str)
allergy_parser.add_argument('description', type=str)
allergy_parser.add_argument('user_id', type=int)



class AllergyResource(Resource):
    @marshal_with(allergy_field)
    def get(self, id = None):
        if id: 
            return Allergy.query.get_or_404(id)
        return Allergy.query.all()
    
    @marshal_with(allergy_field)
    def post(self):
        args = allergy_parser.parse_args()
        allergy = Allergy(name = args['name'], description = args['description'], user_id = args['user_id'])
        db.session.add(allergy)
        db.session.commit()
        allergys = Allergy.query.all()
        return allergys, 201
    
    @marshal_with(allergy_field)
    def patch(self, id):
        args = allergy_parser.parse_args()
        allergy = Allergy.query.filter_by(id = id).first()
        if not allergy:
            abort(404, message = 'Allergy not found')
        if args['name']:
            allergy.name = args['name']
        if args['description']:
            allergy.description = args['description']
        if args['user_id']:
            allergy.user_id = args['user_id']
        return allergy
    
    @marshal_with(allergy_field)
    def delete(self, id):
        allergy = Allergy.query.filter_by(id = id).first()
        if not allergy:
            abort(404, message = 'allergy not found')
        db.session.delete(allergy)
        db.session.commit()
        return '', 204