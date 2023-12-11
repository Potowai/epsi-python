from django.shortcuts import render
from .models import Pokemon
from .utils import import_pokemon_data,import_pokemon_datav2,getPokemonById  

async def pokemon_list(request):
    pokemons = await import_pokemon_datav2(request.GET.get("search", ""))
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, pokeid):
    pokemon = getPokemonById(pokeid)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

