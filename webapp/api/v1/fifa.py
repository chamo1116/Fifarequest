from webapp.api.v1 import api
from flask import request, jsonify
from webapp.exceptions import InternalServerError
from webapp.models.team import Team
import json
# Routes
# Get team by name
@api.route('/search_team/<string:name_team>',  methods=['GET'])
def search_team(name_team):
    try:
        #Instance team with name team
        team = Team({"name":name_team})
        #Search element
        response = team.search()
        return jsonify(team=response)
    except Exception as e:
        raise InternalServerError(e)

# Create team
@api.route('/create_team',  methods=['POST'])
def create_team():
    try:
        data = request.json
        #Create and instance Team
        team = Team(data)
        #Save data in database
        team.save()
        response = jsonify(response="Team created successfully")
        return response
        return jsonify({})
    except Exception as e:
        raise InternalServerError(e)


#Update team
@api.route('/update_team',  methods=['PUT'])
def update_team():
    data = request.json
    update_team = Team(data)
    response = update_team.update()
    return jsonify(updated_team=response)


#Delete team
@api.route('/delete_team',  methods=['DELETE'])
def delete_team():
    try:
        delete_data = request.json
        delete_team_obj = Team(delete_data)
        #Delete by name
        delete_team_obj.remove()
        return jsonify(update_team='Team Deleted')
    except Exception as e:
        raise InternalServerError(e)



#Number of teams
@api.route('/registred_teams',  methods=['GET'])
def registred_teams():
    try:
        team = Team()
        number_teams = team.registred_teams_model(team)
        return jsonify(number_teams=number_teams)
    except Exception as e:
        raise InternalServerError(e)

#Number of players
@api.route('/number_players',  methods=['GET'])
def number_players():
    try:
        team = Team()
        number_players = team.number_players_model(team)
        return jsonify(numberplayers=number_players)
    except Exception as e:
        raise InternalServerError(e)

#Youngest player
@api.route('/youngest_player',  methods=['GET'])
def youngest_player():
    try:
        team = Team()
        youngest_player = team.youngest_player_model(team)
        return jsonify(response=youngest_player)
    except Exception as e:
        raise InternalServerError(e)

#Oldest player
@api.route('/oldest_player',  methods=['GET'])
def oldest_player():
    try:
        team = Team()
        oldest_player = team.oldest_player_model(team)
        return jsonify(response=oldest_player)
    except Exception as e:
        raise InternalServerError(e)

#No headline players
@api.route('/no_headline_players',  methods=['GET'])
def no_headline_players():
    try:
        team = Team()
        number_no_headline_players = team.no_headline_players_model(team)
        return jsonify(number_no_headline_players=number_no_headline_players)
    except Exception as e:
        raise InternalServerError(e)



#Average of no headline players per team
@api.route('/average_no_headline_players',  methods=['GET'])
def average_no_headline_players():
    try:
        team = Team()
        average_per_team = team.average_no_headline_players_model(team)
        return jsonify(average_per_team)
    except Exception as e:
        raise InternalServerError(e)

#Team with more players registred
@api.route('/more_players_team',  methods=['GET'])
def more_players_team():
    try:
        team = Team()
        team_mayor = team.more_players_team_model(team)
        return jsonify(response=team_mayor)
    except Exception as e:
        raise InternalServerError(e)


#Average age players
@api.route('/average_age_players',  methods=['GET'])
def average_age_players():
    try:
        team = Team()
        average = team.average_age_players_model(team)
        return jsonify(average_age=average)
    except Exception as e:
        raise InternalServerError(e)

#Average players per team
@api.route('/average_players_per_team',  methods=['GET'])
def average_players_per_team():
    try:
        team = Team()
        average = team.average_players_per_team_model(team)
        return jsonify(average_players_per_team=average)
    except Exception as e:
        raise InternalServerError(e)

#Coach with different nationality
@api.route('/coach_nationality',  methods=['GET'])
def coach_nationality():
    try:
        team = Team()
        list_coach = team.coach_nationality_model(team)
        return jsonify(list_coach)
    except Exception as e:
        raise InternalServerError(e)


#Oldest coach
@api.route('/oldest_coach',  methods=['GET'])
def oldest_coach():
    try:
        team = Team()
        coach_oldest = team.oldest_coach_model(team)
        return jsonify(coach_oldest=coach_oldest)
    except Exception as e:
        raise InternalServerError(e)

