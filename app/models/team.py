from pymodm import EmbeddedMongoModel, MongoModel, fields
from PIL import Image

#Create Database Model
class Players(EmbeddedMongoModel):
    picture = fields.CharField()
    name = fields.CharField(required = True)
    last_name = fields.CharField(required = True)
    birth_date = fields.DateTimeField(required = True)
    position_player = fields.CharField(required = True)
    number_player = fields.IntegerField()
    headline = fields.BooleanField(required = True)


class Technical_team(EmbeddedMongoModel):
    name = fields.CharField(required = True)
    last_name = fields.CharField()
    birth_date = fields.DateTimeField(required = True)
    nationality = fields.CharField(required = True)
    rol = fields.CharField(
        choices=('coach', 'assistant', 'doctor', 'preparer'), required = True)


class Team(MongoModel):
    name = fields.CharField(primary_key= True, required = True)
    flag = fields.CharField()
    shield = fields.CharField()
    players = fields.EmbeddedModelListField(Players, required = True)
    technical_team = fields.EmbeddedModelListField(Technical_team, required = True)