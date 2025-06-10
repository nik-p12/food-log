from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import HealthReaction
from datetime import date, datetime
from .generic_resource import GenericResource

health_reaction_field = {
    'id': fields.Integer,
    'symptom': fields.String,
    'severity': fields.Integer,
    'delay_after_meal': fields.Float,
    'notes': fields.String,
    'date_reported': fields.String,
    'user_id': fields.Integer,
    'meal_id': fields.Integer
}

health_reaction_parser = reqparse.RequestParser()
health_reaction_parser.add_argument('symptom', type=str)
health_reaction_parser.add_argument('severity', type=int)
health_reaction_parser.add_argument('delay_after_meal', type=float)
health_reaction_parser.add_argument('notes', type=str)
health_reaction_parser.add_argument('meal_id', type=int)
health_reaction_parser.add_argument('user_id', type=int)
health_reaction_parser.add_argument('date_reported', type=str)


class HealthReactionResource(Resource):
    @marshal_with(health_reaction_field)
    def get(self,id = None):
        if id:
            return HealthReaction.query.get_or_404(id)
        return HealthReaction.query.all()
    
    @marshal_with(health_reaction_field)
    def post(self):
        args = health_reaction_parser.parse_args()
        health_reaction = HealthReaction(symptom = args['symptom'],severity = args['severity'], delay_after_meal = args['delay_after_meal'],notes = args['notes'],date_reported =  datetime.strptime(args['date_reported'], "%Y-%m-%d %H:%M:%S"),meal_id = args['meal_id'], user_id = args['user_id'])
        db.session.add(health_reaction)
        db.session.commit()
        health_reactions = HealthReaction.query.all()
        return health_reactions, 201

    @marshal_with(health_reaction_field)
    def patch(self, id):
        args = health_reaction_parser.parse_args()
        health_reaction = HealthReaction.query.filter_by(id = id).first()
        if not health_reaction:
            abort(404, message = "health reaction not found")
        if args['symptom']:
            health_reaction.symptom = args['symptom']
        if args['severity']:
            health_reaction.severity = args['severity']
        if args['delay_after_meal']:
            health_reaction.delay_after_meal = args['delay_after_meal']
        if args['notes']:
            health_reaction.notes = args['notes']
        if args['date_reported']:
            health_reaction.date_deported =  datetime.strptime(args['date_reported'], "%Y-%m-%d %H:%M:%S")
        if args['meal_id']:
            health_reaction.meal_id = args['meal_id']
        if args['user_id']:
            health_reaction.user_id = args['user_id']
        db.session.commit()
        return health_reaction
    
    @marshal_with(health_reaction_field)
    def delete(self, id):
        health_reaction = HealthReaction.query.filter_by(id = id).first()
        if not health_reaction:
            abort(404, message ='health reaction not found')
        db.session.delete(health_reaction)
        db.session.commit()
        return '', 204