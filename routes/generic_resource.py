from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from database.db import db

class GenericResource(Resource):
    def __init__(self, model, parser, fields):
        self.model = model
        self.parser = parser
        self.fields = fields

    @marshal_with(fields)
    def get(self, id=None):
        if id:
            item = self.model.query.get_or_404(id)
            return item
        return self.model.query.all()

    @marshal_with(fields)
    def post(self):
        args = self.parser.parse_args()
        item = self.model(**args)
        db.session.add(item)
        db.session.commit()
        return item, 201

    @marshal_with(fields)
    def put(self, id):
        item = self.model.query.get_or_404(id)
        args = self.parser.parse_args()
        for key, value in args.items():
            setattr(item, key, value)
        db.session.commit()
        return item

    def delete(self, id):
        item = self.model.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return '', 204