from flask import Flask
from webapp.api.v1 import api as api_blueprint


def create_app(app):
    with app.app_context():
        # Blueprint registration
        app.register_blueprint(api_blueprint, url_prefix='/api/v1')
        app.config["MONGO_URI"] = 'mongodb+srv://chamo1116:Chamo%2B2201@cluster0-alr0n.mongodb.net/test?retryWrites=true'
    return app


app = Flask(__name__)
app = create_app(app)






