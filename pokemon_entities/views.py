import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)
        for pokemon_entity in pokemon_entities:
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon_entity.pokemon.photo.url)
                if pokemon_entity.pokemon.photo else ''
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.photo.url if pokemon.photo else '',
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def previous_and_next_evolution(request, type_evolution, text_evolution: str):
    if text_evolution == 'previous_evolution':
        if type_evolution:
            data_evolution = {
                "title_ru": type_evolution.title,
                "pokemon_id": type_evolution.id,
                "img_url": request.build_absolute_uri(
                    type_evolution.photo.url),
            }
        else:
            data_evolution = {}
    elif text_evolution == 'next_evolutions':
        next_pokemon = type_evolution.all().first()
        if next_pokemon:
            data_evolution = {
                "title_ru": next_pokemon.title,
                "pokemon_id": next_pokemon.id,
                "img_url": request.build_absolute_uri(
                    next_pokemon.photo.url),
            }
        else:
            data_evolution = {}

    return data_evolution


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)

    img_url = request.build_absolute_uri(pokemon.photo.url) if \
        pokemon.photo else ''

    previous_evolution = previous_and_next_evolution(request,
                                                     pokemon.previous_evolution,
                                                     'previous_evolution')

    next_evolutions = previous_and_next_evolution(request,
                                                  pokemon.next_evolutions,
                                                  'next_evolutions')

    pokemon_dict = {
        "pokemon_id": pokemon.id,
        "title_ru": pokemon.title,
        "img_url": img_url,
        "description": pokemon.description,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "previous_evolution": previous_evolution,
        "next_evolution": next_evolutions,
    }


    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    pokemon_entities = PokemonEntity.objects.filter(pokemon=pokemon)

    for pokemon_entity in pokemon_entities:
        image_url = request.build_absolute_uri(
            pokemon_entity.pokemon.photo.url) if pokemon_entity.pokemon.photo else ''
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            image_url,
        )

    return render(request, "pokemon.html",
                  context={'map': folium_map._repr_html_(),
                           'pokemon': pokemon_dict})
