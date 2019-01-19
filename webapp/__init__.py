''' flask app with mongo '''
import os
import json
import datetime
from bson.objectid import ObjectId
from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
#from webapp.api.v1 import api as api_blueprint

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://chamo1116:chamito@cluster0-shard-00-00-alr0n.mongodb.net:27017,\
cluster0-shard-00-01-alr0n.mongodb.net:27017,cluster0-shard-00-02-alr0n.mongodb.net:27017/\
test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
app.config['JWT_SECRET_KEY'] = "secret"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
conn = PyMongo(app)
flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.json_encoder = JSONEncoder

from webapp.api.v1 import *







