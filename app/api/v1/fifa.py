from app.api.v1 import api
from flask import request, jsonify
from app.models.team import Team
from app.exceptions import InternalServerError
from pymodm import errors

"""
    Create JSON
    {
        'name': Barcelona,
        'flag':        
    }
"""


#Routes
#Get team by name
@api.route('/search_team/<str:name_team>',  methods=['GET'])
def search_team(name_team):
    try:
        team = Team.objects.get({'name': name_team})
        response = jsonify(team)
        response.status_code = 201
        return response
    except errors.DoesNotExist as e:
        print(e)
        raise InternalServerError(e)


#Create team
@api.route('/create_team',  methods=['POST'])
def create_team():
    try:
        data = request.json
        name = data["name"]
        flag = data["flag"]
        shield = data["shield"]
        players = data["players"]
        technical_team = data["technical_team"]
        new_team = Team.objects.create(name = name, flag=flag, shield=shield, players=players, technical_team=technical_team)
        response = jsonify(new_team)
        return response
    except Exception as e:
        print(e)
        raise InternalServerError(e)

#Update team
@api.route('/update_team',  methods=['PUT'])
def update_team():
    data = request.json
    response = jsonify({'Team created successfull'})
    response.status_code = 201
    return response




