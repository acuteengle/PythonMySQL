from __main__ import app
from flask import request # https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
import PokemonType

'''
Pokemon Type Routes ***
'''

@app.route('/pokemon_type')
def getAllPokemonTypes():
    return PokemonType.getAll()

@app.route('/pokemon_type/<string:id>', methods=['GET'])
def getPokemonTypeById(id):
    return PokemonType.getOne(id)

@app.route('/pokemon_type', methods=['POST'])
def createPokemonType():
    data = request.json
    return PokemonType.createOne(data)

@app.route('/pokemon_type/<string:id>', methods=['PUT'])
def updatePokemonType(id):
    data = request.json
    return PokemonType.updateOne(id, data)
