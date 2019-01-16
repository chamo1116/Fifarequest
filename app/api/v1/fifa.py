from app.api.v1 import api
from app.api.v1.models import Team 


#Routes
@api.route('/create_team',  methods=['POST'])
def create_team():

    return 'hola mundo'
