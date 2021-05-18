from flask import Flask
from . import api
from . import database
from werkzeug.utils import import_string


def create_app():
    app = Flask(__name__)
    app.config.from_object(f"app_config.{app.config['ENV']}")

    api.api.init_app(app)
    database.db.init_app(app)
    database.migrate.init_app(app, database.db)

    return app
