from pymodm import MongoModel, fields

#Create Database Model
class Player(MongoModel):
    picture = fields.CharField()
    name = fields.CharField(required=True)
    last_name = fields.CharField(required=True)
    birth_date = fields.DateTimeField(required=True)
    position_player = fields.CharField(required=True)
    number_player = fields.IntegerField()
    headline = fields.BooleanField(required=True)


class Technical_team(MongoModel):
    name = fields.CharField(required = True)
    last_name = fields.CharField()
    birth_date = fields.DateTimeField(required = True)
    nationality = fields.CharField(required = True)
    rol = fields.CharField(
        choices=('coach', 'assistant', 'doctor', 'preparer'), required=True)


class Team(MongoModel):
    name = fields.CharField(primary_key=True, required=True)
    flag = fields.CharField()
    shield = fields.CharField()
    players = fields.ReferenceField(Player, required=True)
    technical_team = fields.ReferenceField(Technical_team, required=True)