import requests
from .models import Pokemon



def import_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1021"
    response = requests.get(url)
    data = response.json()
    pokeList = []
    for result in data["results"]:
        pokeList.append(Pokemon(
            name=result['name'],
            pokeid = result['url'].rstrip('/').split('/')[-1],
            image_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{result['url'].rstrip('/').split('/')[-1]}.png"
            ))
    print("###########################################    imported")
    return pokeList

def getPokemonByName(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    pokemon_data = response.json()
    return makePokemon(pokemon_data)

def makePokemon(pokemon_data):
    return Pokemon(
            name=pokemon_data["name"],
            pokeid = pokemon_data['id'],
            description="Add your description here.",
            height=pokemon_data["height"],
            weight=pokemon_data["weight"],
            image_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_data['id']}.png")  