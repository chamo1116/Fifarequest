from flask import Flask
from flask import g
from webapp.api.v1 import api as api_blueprint
from flask_pymongo import PyMongo


def create_app(app):
	with app.app_context():
	    # Blueprint registration
	    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
	    app.config["MONGO_URI"]= "mongodb://localhost:27017/fifa_database"
	return app
app = Flask(__name__)
app = create_app(app)






