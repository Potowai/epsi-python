import requests
from django.shortcuts import render
from .models import Pokemon

def import_pokemon_data():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
    data = response.json()
    pokemons = [get_pokemon_by_name(result["name"]) for result in data["results"]]
    return pokemons

def get_pokemon_by_name(_name):
    if Pokemon.objects.filter(name=_name).exists():
        pokemon = Pokemon.objects.get(name=_name)
        print(f"Pokemon {pokemon} already exists in database")
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{_name}"
        response = requests.get(url)
        pokemon_data = response.json()
        pokemon = Pokemon(
            name=pokemon_data["name"],
            pokeid = pokemon_data['id'],
            height=pokemon_data["height"],
            weight=pokemon_data["weight"],
            abilities = [ability['ability']['name'] for ability in pokemon_data["abilities"]],
            types = [ptype['type']['name'] for ptype in pokemon_data["types"]],
            moves = [move['move']['name'] for move in pokemon_data["moves"]],
            stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data["stats"]},
            sprites = pokemon_data["sprites"]["front_default"],
            base_experience=pokemon_data["base_experience"])
        pokemon.save()
        print("Pokemon added to database")
    return pokemon