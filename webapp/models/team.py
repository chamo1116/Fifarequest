from bson import ObjectId
from pymongo import MongoClient
from webapp.exceptions import InternalServerError
import flattener
import itertools
from datetime import datetime, date
from webapp import app, conn
"""
        Create team JSON
        {
                "_id": 1,
                "name_id": "Brasil",
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
                "_id": 2,
                "name_id": "Colombia",
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

class Model(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def save(self):
        self.collection.insert(self)
    def search(self):
        try:
            response = self.collection.find_one({"name": self.name})
            response = self.export_data(response)
            return response
        except Exception as e:
            raise InternalServerError(e)

    def update(self):
        try:
            #Update team
            self.collection.update_one({'name':self.name}, {"$set":self}, upsert=False)
            #Search updated team
            updated_team = self.collection.find_one({'name': self.name})
            response = self.export_data(updated_team)
            return response
        except Exception as e:
            raise InternalServerError(e)

    def remove(self):
        try:
            Team.collection.delete_one({'name':self.name})
            self.clear()
        except Exception as e:
            raise InternalServerError(e)



class Team(Model):
    #Get collection from database
    collection = conn.db.fifa_collections

    @staticmethod
    def export_data(data):
        return {
            'name': data["name"],
            'flag': data["flag"],
            'shield': data["shield"],
            'players': [Player.export_data(player) for player in data["players"]],
            'technical_team': [Technical_team.export_data(technical) for technical in data["technical_team"]]
        }


    @staticmethod
    def registred_teams_model(self):
        try:
            # Get all teams registred
            cursor = self.collection.find({})
            number_teams = 0
            #Go through the database
            for team in cursor:
                if team:
                    #Count each team
                    number_teams += 1
            return number_teams
        except Exception as e:
            raise InternalServerError(e)



    @staticmethod
    def number_players_model(self):
        try:
            # Get all teams registred
            cursor = self.collection.find({})
            number_players = 0
            # Go through the database
            for team in cursor:
                # Get players of each team
                players = team["players"]
                # Accumulate players
                number_players += len(players)
            return number_players
        except Exception as e:
            raise InternalServerError(e)


    @staticmethod
    def youngest_player_model(self):
        try:
            names = []
            birth_dates = []
            # Get all teams registred
            cursor = self.collection.find({})
            for team in cursor:
                #Get players
                players = team["players"]
                for player in players:
                    #Get all names and birth dates in differents lists but with the same index
                    names.append(player["name"]+" "+player["last_name"])
                    birth_dates.append(player["birth_date"])
            index_max_birth_date = birth_dates.index(max(birth_dates))
            youngest_player = names[index_max_birth_date]
            return youngest_player
        except Exception as e:
            raise InternalServerError(e)


    @staticmethod
    def oldest_player_model(self):
        try:
            # Get all teams registred
            names = []
            birth_dates = []
            cursor = self.collection.find({})
            for team in cursor:
                #Get players
                players = team["players"]
                for player in players:
                    #Get all names and birth dates in differents lists but with the same index
                    names.append(player["name"]+" "+player["last_name"])
                    birth_dates.append(player["birth_date"])
            index_min_birth_date = birth_dates.index(min(birth_dates))
            oldest_player = names[index_min_birth_date]
            return oldest_player
        except Exception as e:
            raise InternalServerError(e)


    @staticmethod
    def no_headline_players_model(self):
        try:
            # Get all teams with no headline players
            cursor = self.collection.find({"players.headline": "True"})
            number_no_headline_players = 0
            for team in cursor:
                players = team["players"]
                for player in players:
                    #Look for players who are headline 
                    if player["headline"]=="True":
                        number_no_headline_players += 1
            return number_no_headline_players
        except Exception as e:
            raise InternalServerError(e)


    @staticmethod
    def average_no_headline_players_model(self):
        try:
            # Get all teams with no headline players
            cursor = self.collection.find({"players.headline": "True"})
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
            return average_per_team
        except Exception as e:
            raise InternalServerError(e)


    @staticmethod
    def more_players_team_model(self):
        try:
            # Get all teams 
            cursor = self.collection.find({})
            names = []
            num_players = []
            for team in cursor:
                names.append(team["name"])
                num_players.append(len(team["players"]))
            index_max_team_players = num_players.index(max(num_players))
            team = names[index_max_team_players]
            return team
        except Exception as e:
            raise InternalServerError(e)

    @staticmethod
    def average_age_players_model(self):
        try:
            # Get all teams 
            cursor = self.collection.find({})
            #Start Counters
            players_total = 0
            average = 0
            accum_age = 0
            for team in cursor:
                #Calculate number_players per team
                players = team["players"]
                for player in players:
                    #Calculate age
                    birth_date = player["birth_date"]
                    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
                    today = date.today()
                    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                    accum_age += age
                    players_total+=1
            #Calculate average
            average = round(accum_age/players_total)
            return average
        except Exception as e:
            raise InternalServerError(e)


    @staticmethod
    def average_players_per_team_model(self):
        try:
            # Get all teams 
            cursor = self.collection.find({})
            players_total = 0
            total_teams = 0
            for team in cursor:
                #Calculate number_players per team
                players = team["players"]
                players_total+=len(players)
                total_teams+=1
            #Calculate average
            average = players_total/total_teams
            return average
        except Exception as e:
            raise InternalServerError(e)

    @staticmethod
    def coach_nationality_model(self):
        try:
            # Get fields: team name, coach name, coach last_name and coach nationality 
            cursor = self.collection.find({"technical_team.rol":"Coach"},{ "name": 1, "technical_team.name" : 1, 
                "technical_team.last_name" : 1, "technical_team.nationality" : 1 })
            list_coach = []
            for team in cursor:
                technical_team = team["technical_team"]
                for coach in technical_team:
                    #Validate nationality with the team name
                    if coach["nationality"] != team["name"]:
                        list_coach.append(coach["name"]+" "+coach["last_name"])
            return list_coach
        except Exception as e:
            raise InternalServerError(e)

    @staticmethod
    def oldest_coach_model(self):
        try:
            # Get fields: team name, coach name, coach last_name and birthdate's coach 
            cursor = self.collection.find({"technical_team.rol":"Coach"},{ "name": 1, "technical_team.name" : 1, 
                "technical_team.last_name" : 1, "technical_team.birth_date" : 1 })
            age_coach = []
            name_coach = []
            for team in cursor:
                technical_team = team["technical_team"]
                for coach in technical_team:
                    #Calculate each coach age 
                    birth_date = coach["birth_date"]
                    birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
                    today = date.today()
                    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                    age_coach.append(age)
                    name_coach.append(coach["name"]+" "+coach["last_name"])
            #Calculate max and the index
            index_max_age_coach = age_coach.index(max(age_coach))
            coach_oldest = name_coach[index_max_age_coach]
            return coach_oldest
        except Exception as e:
            raise InternalServerError(e)

class Player:

    @staticmethod
    def export_data(data):
        return {
            'picture': data["picture"],
            'name': data["name"],
            'last_name': data["last_name"],
            'birth_date': data["birth_date"],
            'position_player': data["position_player"],
            'number_player': data["number_player"],
            'headline': data["headline"]
        }


class Technical_team:
    @staticmethod
    def export_data(data):
        return {
            "name": data["name"],
            "last_name": data["last_name"],
            "birth_date": data["birth_date"],
            "nationality": data["nationality"],
            "rol": data["rol"]
        }