from webapp.api.v1 import api
from flask import request, jsonify
from webapp.exceptions import InternalServerError
from webapp.models.team import Team
import json
import flattener
import itertools
from datetime import datetime, date
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
                "name": "Brasil",
                "flag": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj3tJKe8vjfAhUKTt8KHfllC8AQjRx6BAgBEAU&url=http%3A%2F%2Fwww.banderas-mundo.es%2Fbrasil&psig=AOvVaw0KdN1kDSFmt5pXoFQLm8yd&ust=1547954556550458",
                "shield": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjtrP6z8vjfAhURhOAKHQcXAr8QjRx6BAgBEAU&url=https%3A%2F%2Fcolombia.as.com%2Fresultados%2Fficha%2Fequipo%2Fbrasil%2F1881%2F&psig=AOvVaw0RhdhHWgs5xYOm0AoaAsHW&ust=1547954602396196",
                "players": [
                    {
                        "picture": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwibz_Tm8vjfAhXwUt8KHRSyBCUQjRx6BAgBEAU&url=https%3A%2F%2Fwww.skysports.com%2Ffootball%2Fnews%2F11095%2F11609612%2Ftransfer-talk-podcast-could-neymar-and-philippe-coutinho-be-swapped&psig=AOvVaw1jexXzzuaHt2p8eqeSBW1p&ust=1547954703725864",
                        "name": "Neymar da Silva",
                        "last_name": "Santos",
                        "birth_date": "1992-02-5",
                        "position_player": "Volante",
                        "number_player": 10,
                        "headline": true
                    },
                    {
                        "picture": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjj98HB8_jfAhVhh-AKHcwlC7MQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FThiago_Silva&psig=AOvVaw1HqJnk8X0OeJjYh283yuwH&ust=1547954897821329",
                        "name": "Thiago",
                        "last_name": "Silva",
                        "birth_date": "1984-09-22",
                        "position_player": "Defensa",
                        "number_player": 5,
                        "headline": "False"
                    }
                ],
                "technical_team": [
                    {
                        "name": "Adenor",
                        "last_name": "Bachi",
                        "birth_date": "1961-05-21",
                        "nationality": "Brasil",
                        "rol": "Coach"
                    }
                ]
            }

            {
                "name": "Colombia",
                "flag": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwjl9bD89PjfAhVFON8KHZBzBQcQjRx6BAgBEAU&url=https%3A%2F%2Fwww.comprarbanderas.es%2Fbandera-colombia-presidencial-id46.html&psig=AOvVaw3KtSuoq6-zJO9722wWLbnx&ust=1547955290671553",
                "shield": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjG8I-H9fjfAhWPm-AKHVGAASwQjRx6BAgBEAU&url=https%3A%2F%2Fes.wikipedia.org%2Fwiki%2FEscudo_de_Colombia&psig=AOvVaw1cMHwfzVmfKEq4eMxjxzJk&ust=1547955312446893",
                "players": [
                    {
                        "picture": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiglfag9fjfAhVrQt8KHdcZAhAQjRx6BAgBEAU&url=https%3A%2F%2Fwww.rcnradio.com%2Fdeportes%2Ffutbol-internacional%2Ffalcao-destino-real-madrid&psig=AOvVaw20MG1CyTDhieOsYCStQBj2&ust=1547955365254318",
                        "name": "Falcao",
                        "last_name": "Garcia",
                        "birth_date": "1986-02-10",
                        "position_player": "Delantero",
                        "number_player": 9,
                        "headline": "True"
                    },
                    {
                        "picture": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiLhLuA9vjfAhWmSt8KHbkqDn8QjRx6BAgBEAU&url=%2Furl%3Fsa%3Di%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dimages%26cd%3D%26ved%3D%26url%3Dhttp%253A%252F%252Fdiariodelcauca.com.co%252Fnoticias%252Fdeportes%252Ff%2525C3%2525BAtbol%252Fcamilo-vargas-seguira-en-el-cali-el-portero-podria-llegar-461894%26psig%3DAOvVaw0Qx_kl20mL1pBpKqtJVWZN%26ust%3D1547955564604301&psig=AOvVaw0Qx_kl20mL1pBpKqtJVWZN&ust=1547955564604301",
                        "name": "Camilo",
                        "last_name": "Vargas",
                        "birth_date": "1989-03-09",
                        "position_player": "Arquero",
                        "number_player": 2,
                        "headline": "False"
                    }
                ],
                "technical_team": [
                    {
                        "name": "Jose",
                        "last_name": "Pekerman",
                        "birth_date": "1949-09-03",
                        "nationality": "Colombia",
                        "rol": "Coach"
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
                "name": "Brasil",
                "flag": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj3tJKe8vjfAhUKTt8KHfllC8AQjRx6BAgBEAU&url=http%3A%2F%2Fwww.banderas-mundo.es%2Fbrasil&psig=AOvVaw0KdN1kDSFmt5pXoFQLm8yd&ust=1547954556550458",
                "shield": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjtrP6z8vjfAhURhOAKHQcXAr8QjRx6BAgBEAU&url=https%3A%2F%2Fcolombia.as.com%2Fresultados%2Fficha%2Fequipo%2Fbrasil%2F1881%2F&psig=AOvVaw0RhdhHWgs5xYOm0AoaAsHW&ust=1547954602396196",
                "players": [
                    {
                        "picture": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwibz_Tm8vjfAhXwUt8KHRSyBCUQjRx6BAgBEAU&url=https%3A%2F%2Fwww.skysports.com%2Ffootball%2Fnews%2F11095%2F11609612%2Ftransfer-talk-podcast-could-neymar-and-philippe-coutinho-be-swapped&psig=AOvVaw1jexXzzuaHt2p8eqeSBW1p&ust=1547954703725864",
                        "name": "Neymar da Silva",
                        "last_name": "Santos",
                        "birth_date": "1992-02-5",
                        "position_player": "Volante",
                        "number_player": 10,
                        "headline": true
                    },
                    {
                        "picture": "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjj98HB8_jfAhVhh-AKHcwlC7MQjRx6BAgBEAU&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FThiago_Silva&psig=AOvVaw1HqJnk8X0OeJjYh283yuwH&ust=1547954897821329",
                        "name": "Thiago",
                        "last_name": "Silva",
                        "birth_date": "1984-09-22",
                        "position_player": "Defensa",
                        "number_player": 5,
                        "headline": "False"
                    }
                ],
                "technical_team": [
                    {
                        "name": "Adenor",
                        "last_name": "Bachi",
                        "birth_date": "1961-05-21",
                        "nationality": "Brasil",
                        "rol": "Coach"
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
        number_no_headline_players = 0
        for team in cursor:
        	players = team["players"]
        	for player in players:
        		#Look for players who are headline 
        		if player["headline"]=="True":
        			number_no_headline_players += 1
        return jsonify(number_no_headline_players=number_no_headline_players)
    except Exception as e:
        raise InternalServerError(e)



#Average of no headline players per team
@api.route('/average_no_headline_players',  methods=['GET'])
def average_no_headline_players():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({"players.headline": "True"})
        average_per_team = []
        for team in cursor:
        	average = 0
        	accum = 0
        	players = team["players"]
        	for player in players:
        		#Look for players who are headline 
        		if player["headline"]=="True":
                    #Accum for calculate average below
        			accum += 1
            #Calculate average
        	average = accum/len(players)
            #Insert to a list [team,average]
        	average_per_team.append([team["name"],average])
        #Flatten list
        average_per_team = flattener.flatten(average_per_team)
        #Convert to a dict
        average_per_team = dict(itertools.zip_longest(*[iter(average_per_team)] * 2, fillvalue=""))
        return jsonify(average_per_team)
    except Exception as e:
        raise InternalServerError(e)

#Team with more players registred
@api.route('/more_players_team',  methods=['GET'])
def more_players_team():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({})
        names = []
        num_players = []
        for team in cursor:
            names.append(team["name"])
            num_players.append(len(team["players"]))
        index_max_team_players = num_players.index(max(num_players))
        team = names[index_max_team_players]
        return jsonify(response=team)
    except Exception as e:
        raise InternalServerError(e)


#Average age players
@api.route('/average_age_players',  methods=['GET'])
def average_age_players():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({})
        players_total = 0
        for team in cursor:
            #Start Counters
            average = 0
            accum_age = 0
            #Calculate number_players per team
            players = team["players"]
            players_total+=len(players)
            for player in players:
                #Calculate age
                birth_date = player["birth_date"]
                birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
                today = date.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                accum_age += age
        #Calculate average
        average = accum_age/players_total
        return jsonify(average_age=average)
    except Exception as e:
        raise InternalServerError(e)

#Average players per team
@api.route('/average_players_per_team',  methods=['GET'])
def average_players_per_team():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({})
        players_total = 0
        total_teams = 0
        for team in cursor:
            #Calculate number_players per team
            players = team["players"]
            players_total+=len(players)
            total_teams+=1
        #Calculate average
        average = players_total/total_teams
        return jsonify(average_players_per_team=average)
    except Exception as e:
        raise InternalServerError(e)

#Coach with different nationality
@api.route('/coach_nationality',  methods=['GET'])
def coach_nationality():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({"technical_team.rol":"Coach"},{ "name": 1, "technical_team.name" : 1, 
            "technical_team.last_name" : 1, "technical_team.nationality" : 1 })
        list_coach = []
        for team in cursor:
            technical_team = team["technical_team"]
            for coach in technical_team:
                if coach["nationality"] == team["name"]:
                    list_coach.append(coach["name"]+" "+coach["last_name"])
        return jsonify(list_coach)
    except Exception as e:
        raise InternalServerError(e)


#Oldest coach
@api.route('/oldest_coach',  methods=['GET'])
def oldest_coach():
    try:
        # Get all teams with no headline players
        cursor = Team.collection.find({"technical_team.rol":"Coach"},{ "name": 1, "technical_team.name" : 1, 
            "technical_team.last_name" : 1, "technical_team.birth_date" : 1 })
        age_coach = []
        name_coach = []
        for team in cursor:
            technical_team = team["technical_team"]
            for coach in technical_team:
                birth_date = coach["birth_date"]
                birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
                today = date.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                age_coach.append(age)
                name_coach.append(coach["name"]+" "+coach["last_name"])
        index_max_age_coach = age_coach.index(max(age_coach))
        coach_oldest = name_coach[index_max_age_coach]
        return jsonify(coach_oldest=coach_oldest)
    except Exception as e:
        raise InternalServerError(e)

