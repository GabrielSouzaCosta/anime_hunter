from django.shortcuts import render
from .scripts.animes import search_anime, get_anime, get_top_animes, get_upcoming_animes
import asyncio
from pprint import pprint

def homepage(request):
    return render (request, 'animes/index.html')

def search_animes_view(request):
    animes = asyncio.run(search_anime(request.GET['query']))
    return render(request, 'animes/search_result.html', {'animes': animes})

def anime_details(request, id):
    anime = get_anime(id)
    if anime['episodes']:
        episodes = range(anime['episodes'])
    else:
        episodes = ['Still launching']
    return render(request, 'animes/anime_details.html', {'anime':anime, 'range': episodes })

def top_animes(request):
    animes = get_top_animes()
    pprint(animes)
    return render(request, 'animes/top_animes.html', {'animes': animes})

def upcoming_animes(request):
    animes = get_upcoming_animes()
    pprint(animes)
    return render(request, 'animes/upcoming_animes.html', {'animes': animes})
