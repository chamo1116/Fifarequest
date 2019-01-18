from bson import ObjectId
from pymongo import MongoClient

"""
        JSON
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

#connect to MongoDB.
uri = "mongodb://chamo1116:chamito@cluster0-shard-00-00-alr0n.mongodb.net:27017,cluster0-shard-00-01-alr0n.mongodb.net:27017,\
        cluster0-shard-00-02-alr0n.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true"
#uri = 'mongodb+srv://chamo1116:'+urllib.parse.quote('Chamo+2201', safe='')+\
        #'@cluster0-alr0n.mongodb.net/test?retryWrites=true'
conn = MongoClient(uri)

class Model(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def save(self):
        if not self._id:
            self.collection.insert(self)
        else:
            self.collection.update(
                { "_id": ObjectId(self._id) }, self)

    def reload(self):
        if self._id:
            self.update(self.collection\
                    .find_one({"_id": ObjectId(self._id)}))

    def remove(self):
        if self._id:
            self.collection.remove({"_id": ObjectId(self._id)})
            self.clear()


class Team(Model):
    collection = conn["test"]["fifa_collections"]

    @staticmethod
    def export_data(data):
        return {
            'name': data["name"],
            'flag': data["flag"],
            'shield': data["shield"],
            'players': [Player.export_data(player) for player in data["players"]],
            'technical_team': [Technical_team.export_data(technical) for technical in data["technical_team"]]
        }

    @property
    def keywords(self):
        return self.title.split()


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