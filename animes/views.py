from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .scripts.animes import search_anime, get_anime, get_top_animes, get_upcoming_animes
import asyncio
from pprint import pprint
from django.contrib.auth.decorators import login_required
from .models import Favorite, Watchlist_item

def homepage(request):
    return render (request, 'animes/index.html')

def search_animes_view(request):
    animes = asyncio.run(search_anime(request.GET['query']))
    return render(request, 'animes/search_result.html', {'animes': animes})

def anime_details(request, id):
    anime = get_anime(id)
    is_favorite = Favorite.objects.filter(anime_id = anime['mal_id'], user = request.user).exists()
    if anime['episodes']:
        episodes = range(anime['episodes'])
    else:
        episodes = ['Still launching']
    return render(request, 'animes/anime_details.html', {'anime':anime, 'range': episodes, 'is_favorite': is_favorite })

def top_animes(request):
    animes = get_top_animes()
    return render(request, 'animes/top_animes.html', {'animes': animes})

def upcoming_animes(request):
    animes = get_upcoming_animes()
    return render(request, 'animes/upcoming_animes.html', {'animes': animes})

@login_required
def add_favorite(request, anime_id):
    if request.method == 'POST':
        favorite = Favorite(anime_id = anime_id, name = request.POST['name'], image_url = request.POST['image_url'], user = request.user)
        if not favorite.is_in_user_list():
            favorite.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')
        return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')

@login_required
def add_to_watchlist(request, anime_id):
    if request.method == 'POST':
        item = Watchlist_item(anime_id = anime_id, name = request.POST['name'], image_url = request.POST['image_url'] , user = request.user)
        if not item.is_in_user_list():
            item.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')
        return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')

@login_required
def remove_favorite(request, anime_id):
    if request.method == 'POST':
        favorite = Favorite.objects.filter(anime_id = anime_id, user = request.user).first()
        if favorite:
            favorite.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'], 'animes:homepage')
        
