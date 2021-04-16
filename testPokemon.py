import unittest
import json
from getData import GetData

class TestPokemon(unittest.TestCase):
    def test_search_valid_pokemon(self):
        my_data = GetData()
        #pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/kakuna')
        pokemon = my_data.get('kakuna')
        my_pokemon = pokemon.json()
        with open('kakuna.json') as kakuna:
            data = json.load(kakuna)
        #moves = ['string-shot', 'harden', 'iron-defense', 'bug-bite', 'electroweb']
        self.assertEqual(200, pokemon.status_code)
        self.assertEqual(data['weight'], my_pokemon['weight'])
        for i in my_pokemon['moves']:
            print(i['move']['name'])
            self.assertTrue(i['move'], ['name'] in data['moves'])

    def test_search_pokemon_by_number(self):
        my_data = GetData()
        pokemon = my_data.get('1')
        my_pokemon = pokemon.json()
        self.assertEqual(200, pokemon.status_code)
        self.assertEqual(my_pokemon['name'], 'bulbasaur')