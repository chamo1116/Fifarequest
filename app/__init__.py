from flask import Flask
from app.api.v1 import api as api_blueprint
from config import Config
from flask_pymongo import PyMongo


def create_app(app):

    # registrando el blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app


app = Flask(__name__)
app.config.from_object(Config)
app = create_app(app)

mongo = PyMongo(app)



