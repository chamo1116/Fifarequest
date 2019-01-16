from app.api.v1 import api
from flask import request, jsonify
from app.models.team import Team
from app.exceptions import InternalServerError
from pymodm import errors
from flask_pymongo import PyMongo
import app


# Routes
# Get team by name
@api.route('/search_team/<string:name_team>',  methods=['GET'])
def search_team(name_team):
    try:
        team = Team.objects.get({'name': name_team})
        response = jsonify(team)
        response.status_code = 201
        return response
    except errors.DoesNotExist as e:
        print(e)
        raise InternalServerError(e)


# Create team
@api.route('/create_team',  methods=['POST'])
def create_team():
    """
        Create team JSON
        {
            "name": "Barcelona",
            "flag": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjg8bPI5fLfAhVSxVkKHZ9YDIgQjRx6BAgBEAU&url=http%3A%2F%2Fwww.disfrutalogratis.com%2Ffc-barcelona.htm&psig=AOvVaw3P5YmWetPnsp3djBqcQe9p&ust=1547744982601549",
            "shield": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiOhpjc5fLfAhVSnFkKHfeaBDQQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFlag_of_Barcelona&psig=AOvVaw2xr7VU8MhVO7MwmGA03c7O&ust=1547745030947326",
            "players": [
                {
                    "picture": "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2018/02/25/15195623621345.jpg",
                    "name": "Leonel",
                    "last_name": "Messi",
                    "birth_date": "1987-06-24",
                    "position_player": "volante creador",
                    "number_player": 10,
                    "headline": true
                }
            ],
            "technical_team": [
                {
                    "name": "Ernesto",
                    "last_name": "Valverde",
                    "birth_date": "1964-02-09",
                    "nationality": "Español",
                    "rol": "coach"
                }
            ]
        }
    """
    try:
        data = request.json
        name = data["name"]
        flag = data["flag"]
        shield = data["shield"]
        players = data["players"]
        technical_team = data["technical_team"]
        mongo = PyMongo(app, )
        new_team = mongo.db.Team.objects.create(name=name, flag=flag, shield=shield, players=players,
                                                technical_team=technical_team)
        response = jsonify(new_team)
        return response
    except Exception as e:
        raise InternalServerError(e)


#Update team
@api.route('/update_team',  methods=['PUT'])
def update_team():
    data = request.json
    response = jsonify({'Team created successfull'})
    response.status_code = 201
    return response




