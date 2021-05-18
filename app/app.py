from flask import Flask
from . import api


def create_app():
    app = Flask(__name__)

    api.api.init_app(app)

    return app
