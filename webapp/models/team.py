from bson import ObjectId
from pymongo import MongoClient
import ssl
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
    @property
    def keywords(self):
        return self.title.split()
