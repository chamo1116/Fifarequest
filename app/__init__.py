from flask import Flask
from app.api.v1 import api as api_blueprint
from config import Config
from pymodm import connect, fields, MongoModel
from pymongo import MongoClient



def create_app(app):

    # Bluepprint rgistration 
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app


app = Flask(__name__)
app.config.from_object(Config)
app = create_app(app)

#Connect to database
mongo = MongoClient(app)
db = client.fifa_database




