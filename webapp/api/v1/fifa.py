from webapp.api.v1 import api
from flask import request, jsonify
from webapp.exceptions import InternalServerError
from webapp.models.team import Team



# Routes
# Get team by name
@api.route('/search_team/<string:name_team>',  methods=['GET'])
def search_team(name_team):
    try:
        #Search Team
        team = Team.collection.find_one({'name': name_team})
        #Export data for sending
        response = Team.export_data(team)
        return jsonify(team=response)
    except Exception as e:
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
        #Create and instance Team
        team = Team(data)
        #Save data in database
        team.save()
        response = jsonify(response="Team created successfully")
        return response
    except Exception as e:
        raise InternalServerError(e)


#Update team
@api.route('/update_team',  methods=['PUT'])
def update_team():
    """
            Update team JSON
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
    update_team = request.json
    #Get team name for filter
    name = update_team["name"]
    #Update team
    Team.collection.update_one({'name':name}, {"$set":update_team}, upsert=False)
    #Search updated team
    updated_team = Team.collection.find_one({'name': name})
    response = Team.export_data(updated_team)
    return jsonify(updated_team=response)


#Delete team
@api.route('/delete_team',  methods=['DELETE'])
def delete_team():
    try:
        delete_team = request.json
        #Get name to delete
        name = delete_team["name"]
        #Delete for name
        Team.collection.delete_one({'name':name})
        return jsonify(update_team='Team Deleted')
    except Exception as e:
        raise InternalServerError(e)



#Number of teams
@api.route('/registred_teams',  methods=['GET'])
def registred_teams():
    try:
        # Get all teams registred
        cursor = Team.collection.find({})
        number_teams = 0
        #Go through the database
        for team in cursor:
            if team:
                #Count each team
                number_teams += 1
        return jsonify(number_teams=number_teams)
    except Exception as e:
        raise InternalServerError(e)

#Number of players
@api.route('/number_players',  methods=['GET'])
def number_players():
    try:
        # Get all teams registred
        cursor = Team.collection.find({})
        number_players = 0
        # Go through the database
        for team in cursor:
            # Get players of each team
            players = team["players"]
            # Accumulate players
            number_players += len(players)
        return jsonify(numberplayers=number_players)
    except Exception as e:
        raise InternalServerError(e)

#Youngest player
@api.route('/youngest_player',  methods=['GET'])
def youngest_player():
    try:
        # Get all teams registred
        names = []
        birth_dates = []
        cursor = Team.collection.find({})
        for team in cursor:
            #Get players
            players = team["players"]
            for player in players:
                #Get all names and birth dates in differents lists but with the same index
                names.append(player["name"]+" "+player["last_name"])
                birth_dates.append(player["birth_date"])
        index_max_birth_date = birth_dates.index(max(birth_dates))
        youngest_player = names[index_max_birth_date]
        return jsonify(response=youngest_player)
    except Exception as e:
        raise InternalServerError(e)

#Oldest player
@api.route('/oldest_player',  methods=['GET'])
def oldest_player():
    try:
        # Get all teams registred
        names = []
        birth_dates = []
        cursor = Team.collection.find({})
        for team in cursor:
            #Get players
            players = team["players"]
            for player in players:
                #Get all names and birth dates in differents lists but with the same index
                names.append(player["name"]+" "+player["last_name"])
                birth_dates.append(player["birth_date"])
        index_min_birth_date = birth_dates.index(min(birth_dates))
        youngest_player = names[index_min_birth_date]
        return jsonify(response=youngest_player)
    except Exception as e:
        raise InternalServerError(e)

#No headline players
@api.route('/no_headline_players',  methods=['GET'])
def no_headline_players():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({"players.headline": "True"})
        teams = []
        for team in cursor:
            team = Team.export_data(team)
            teams.append(team)
        number_no_headline_players = len(teams)
        return jsonify(number_no_headline_players=number_no_headline_players)
    except Exception as e:
        raise InternalServerError(e)




