from flask_restx import Namespace, Resource
from . import models
from app import database
from app.database import Sample


api = Namespace("samples")


@api.route("")
class SampleResource(Resource):

    @database.session
    @api.expect(models.sample(api))
    def post(self, session):
        session.add(Sample(**api.payload))
        return

    @database.session
    @api.marshal_list_with(models.sample(api))
    def get(self, session):
        return session.query(Sample).all()
