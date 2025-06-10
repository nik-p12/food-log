from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db
from models import HealthIssue
from datetime import date, datetime
from .generic_resource import GenericResource

health_issue_field = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'diagnosed_by': fields.String,
    'date_diagnosed': fields.String,
    'user_id': fields.Integer
}

health_issue_parser = reqparse.RequestParser()
health_issue_parser.add_argument('name', type=str)
health_issue_parser.add_argument('description', type=str)
health_issue_parser.add_argument('diagnosed_by', type=str)
health_issue_parser.add_argument('date_diagnosed', type=str)
health_issue_parser.add_argument('user_id', type=int)

class HealthIssueResource(Resource):
    @marshal_with(health_issue_field)
    def get(self, id = None):
        if id:
            return HealthIssue.query.get_or_404(id)
        return HealthIssue.query.all()
    
    @marshal_with(health_issue_field)
    def post(self):
        args = health_issue_parser.parse_args()
        health_issue = HealthIssue(name = args['name'], description = args['description'], diagnosed_by = args['diagnosed_by'], date_diagnosed =  datetime.strptime(args['date_diagnosed'], "%Y-%m-%d"), user_id = args['user_id'])
        db.session.add(health_issue)
        db.session.commit()
        health_issues = HealthIssue.query.all()
        return health_issues, 201
    
    @marshal_with(health_issue_field)
    def patch(self, id):
        args = health_issue_parser.parse_args()
        health_issue = HealthIssue.query.filter_by(id = id).first()
        if not health_issue:
            abort(404, message = 'health issue not found')
        if args['name']:
            health_issue.name = args['name']
        if args['description']:
            health_issue.description = args['description']
        if args['diagnosed_by']:
            health_issue.diagnostised_by = args['diagnostised_by']
        if args['date_diagnosed']:
            health_issue.date_diagnosed = args['date_diagnosed']
        if args['user_id']:
            health_issue.user_id = args['user_id']
        db.session.commit()
        return health_issue
    
    @marshal_with(health_issue_field)
    def delete(self, id):
        health_issue = HealthIssue.query.filter_by(id = id).first()
        if not health_issue:
            abort(404, message = 'health issues ')
        db.session.delete(health_issue)
        db.session.commit()
        return '', 204