from __main__ import app
from flask import request
import Pokemon

'''
Pokemon Routes ***
'''

@app.route('/pokemon')
def getAllPokemon():
    return Pokemon.getAll()

@app.route('/pokemon/<string:id>', methods=['GET'])
def getPokemonById(id):
    return Pokemon.getOne(id)

@app.route('/pokemon', methods=['POST'])
def createPokemon():
    data = request.form
    return Pokemon.createOne(data)

@app.route('/pokemon/<string:id>', methods=['PUT'])
def updatePokemon(id):
    data = request.form
    return Pokemon.updateOne(id, data)