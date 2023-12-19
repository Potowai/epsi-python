from django.shortcuts import render
from .models import Pokemon
from .utils import import_pokemon_data, get_pokemon_by_name

def pokemon_list(request):
    # Ensure that the import_pokemon_data function is async-compatible
    # If it's not, you'll need to refactor it to be async or run it in a sync_to_async wrapper
    pokemons = import_pokemon_data()
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, name):
    # get_pokemon_by_name must be an async function if you're using it with await
    # If it performs synchronous ORM operations, you'll need to wrap those operations with sync_to_async
    pokemon = get_pokemon_by_name(name)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})
