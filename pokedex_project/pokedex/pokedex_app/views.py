from django.shortcuts import render, get_object_or_404
from .models import Pokemon
from .utils import import_pokemon_data,getPokemonByName  

def pokemon_list(request):
    pokemons = import_pokemon_data()
    print(pokemons)
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, name):
    pokemon = getPokemonByName(name)
    print(pokemon)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

