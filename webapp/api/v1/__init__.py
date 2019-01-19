from flask import Blueprint


api = Blueprint('api', __name__)


@api.before_request
def before_request():
    pass


@api.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


from webapp.api.v1 import fifa
from webapp.api.v1 import user_controller