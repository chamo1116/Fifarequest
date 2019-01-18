from flask import Flask, g
from webapp.api.v1 import api as api_blueprint


def create_app(app):
	with app.app_context():
		# Blueprint registration
		app.register_blueprint(api_blueprint, url_prefix='/api/v1')
	return app

app = Flask(__name__)
app = create_app(app)






