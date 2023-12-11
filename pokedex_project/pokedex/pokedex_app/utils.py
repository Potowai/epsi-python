import requests
import httpx
from .models import Pokemon

async def all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1293"
    async with httpx.AsyncClient() as httpx_client:
        response = await httpx_client.get(url)
        data = response.json()
        pokemons = []
        for result in data["results"]:
            pokemons.append(Pokemon(
                name=result['name'],
                url="https://pokeapi.co/api/v2/pokemon/" + result['name'],
                pokeid = result['url'].rstrip('/').split('/')[-1],
                image_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{result['url'].rstrip('/').split('/')[-1]}.png"
                ))
    return pokemons

async def fetch_pokemon_by_search(search):
    all_pokemons = await all_pokemon()
    return searchPokemons(all_pokemons, search)


async def import_pokemon_datav2(search=""):
    pokemons = []
    fetched = await fetch_pokemon_by_search(search)
    if len(fetched) > 0 :
        # Limitation des appels à l'API pour les 20 premiers Pokémon
        async with httpx.AsyncClient() as httpx_client:
            for i in range(0, len(fetched)):
                pokemon_data = await httpx_client.get(fetched[i]['url'])
                if pokemon_data.status_code == httpx.codes.OK:
                    pokemons.append(makePokemon(capitalize_json(pokemon_data.json())))      
    return pokemons 

def import_pokemon_data():
    print("###########################################    import_pokemon_data")
    url = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=10000"
    response = requests.get(url)
    data = response.json()
    pokeList = []
    for result in data["results"]:
        pokeList.append(Pokemon(
            name=result['name'],
            pokeid = result['url'].rstrip('/').split('/')[-1],
            image_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{result['url'].rstrip('/').split('/')[-1]}.png"
            ))
    return pokeList

def getPokemonById(pokeid):
    print("###########################################    getPokemonById")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokeid}"
    response = requests.get(url)
    #capitalize the first letter of every value in the dictionary in one line
    pokemon_data = response.json()
    pokemon_data = capitalize_json(pokemon_data)
    return makePokemon(pokemon_data)

def makePokemon(pokemon_data):
    return Pokemon(
            name=pokemon_data["name"],
            pokeid = pokemon_data['id'],
            description="Add your description here.",
            height=pokemon_data["height"],
            weight=pokemon_data["weight"],
            abilities=pokemon_data["abilities"],
            types=pokemon_data["types"],
            moves=pokemon_data["moves"],
            stats=pokemon_data["stats"],
            sprites=pokemon_data["sprites"],
            base_experience=pokemon_data["base_experience"],
            image_url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_data['id']}.png")  

def capitalize_json(json_data):
    if isinstance(json_data, dict):
        return {key: capitalize_json(value) for key, value in json_data.items()}
    elif isinstance(json_data, list):
        return [capitalize_json(item) for item in json_data]
    elif isinstance(json_data, str):
        return json_data.capitalize()
    else:
        return json_data

def findMostAccuratePokemons(pokemons, search):
    def calculate_score(pokemon):
        name = pokemon.name.lower()
        s = search.lower()
        index = name.find(s)
        if index == -1:
            return 0
        elif index == 0:
            return len(s) / len(name)
        else:
            return len(s) / (len(name) + index)

    scores = [calculate_score(pokemon) for pokemon in pokemons]

    pokeScore = [{
        'name': pokemon.name,
        'url': pokemon.url,
        'score': score
    } for pokemon, score in zip(pokemons, scores)]
    sortedPokemons = sorted(pokeScore, key=lambda x: x['score'], reverse=True)
    print(sortedPokemons[0])
    return [pokemon for pokemon in sortedPokemons if pokemon['score'] > 0]

def searchPokemons(pokemons, inputText, maxResults=20):
    print("input text : ", inputText)
    if inputText == "":
        print("input text is empty")
        return pokemons[:maxResults]
    return findMostAccuratePokemons(pokemons, inputText)[:maxResults]