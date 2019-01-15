from app.api.v1 import api


@api.route('/',  methods=['GET'])
def hola_mundo():
    return 'hola mundo'
