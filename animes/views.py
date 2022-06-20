from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .scripts.animes import search_anime, get_anime, get_top_animes, get_upcoming_animes
import asyncio
from pprint import pprint
from django.contrib.auth.decorators import login_required
from .models import Favorite, Watchlist_item
from django.core.paginator import Paginator
from django.views.decorators.clickjacking import xframe_options_exempt

def homepage(request):
    return render (request, 'animes/index.html')

def search_animes_view(request):
    if request.GET['query']:
        query = request.GET.get('query')
        animes = asyncio.run(search_anime(request.GET['query']))
        paginator = Paginator(animes, 24)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'animes/search_result.html', {'animes': page_obj, 'query': query})
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

@xframe_options_exempt
def anime_details(request, id):
    anime = get_anime(id)['data']

    context = {}
    if request.user and request.user.is_anonymous == False:
        is_favorite = Favorite.objects.filter(anime_id = id, user = request.user).exists()
        is_on_watchlist = Watchlist_item.objects.filter(anime_id = id, user = request.user).exists()
        if is_favorite:
            episodes_watched = Favorite.objects.filter(anime_id = id, user = request.user).first().episodes_watched
        elif is_on_watchlist:
            episodes_watched = Watchlist_item.objects.filter(anime_id = id, user = request.user).first().episodes_watched
        else:
            episodes_watched = 0
        context = {'is_favorite': is_favorite, 'is_on_watchlist': is_on_watchlist, 'episodes_watched': episodes_watched }
    try:
        if anime['episodes'] != 0: 
            if anime['episodes'] == 1:
                episodes = range(1, anime['episodes'] + 1)
            else:
                episodes = range(1, anime['episodes'])
            context['range'] = episodes
    except:
        context['range'] = []

    context['anime'] = anime
    return render(request, 'animes/anime_details.html', context=context)

@xframe_options_exempt
def top_animes(request):
    animes = get_top_animes()
    return render(request, 'animes/top_animes.html', {'animes': animes})

def upcoming_animes(request):
    animes = get_upcoming_animes()
    return render(request, 'animes/upcoming_animes.html', {'animes': animes})

@xframe_options_exempt
def discover(request):
    # Render a page with random animes
    animes = get_upcoming_animes()
    return render(request, 'animes/discover.html', {'animes': animes})

@login_required
def add_favorite(request, anime_id):
    if request.method == 'POST':
        favorite = Favorite(
            anime_id = anime_id, 
            name = request.POST['name'], 
            image_url = request.POST['image_url'], 
            user = request.user, 
            episodes_watched = request.POST["episodes"]
            )
        if not favorite.is_in_user_list():
            favorite.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def add_to_watchlist(request, anime_id):
    if request.method == 'POST':
        try:
            episodes = request.POST['episodes']
        except:
            episodes = 0
        item = Watchlist_item(
            anime_id = anime_id,
            name = request.POST['name'], 
            image_url = request.POST['image_url'], 
            user = request.user,
            episodes = episodes
            )
        if not item.is_in_user_list():
            item.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_favorite(request, anime_id):
    if request.method == 'POST':
        favorite = Favorite.objects.filter(anime_id = anime_id, user = request.user).first()
        if favorite:
            favorite.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def remove_from_watchlist(request, anime_id):
    if request.method == 'POST':
        item = Watchlist_item.objects.filter(anime_id = anime_id, user = request.user).first()
        if item:
            item.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def set_episodes(request, anime_id):
    if request.method == 'POST':
        if request.POST['is_favorite'] == 'True':
            item = Favorite.objects.filter(anime_id = anime_id, user = request.user).first()
            item.episodes_watched = request.POST['episode']
            item.save()
        if request.POST['is_on_watchlist'] == 'True':
            item = Watchlist_item.objects.filter(anime_id = anime_id, user = request.user).first()
            item.episodes_watched = request.POST['episode']
            item.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
        
    return HttpResponseRedirect(request.META['HTTP_REFERER'])    

@xframe_options_exempt
def favorites_test(request):
    animes = get_top_animes()[:5]
    context = {'tiers': ['S', 'A', 'B'], 'favorites': animes}
    return render(request, 'animes/favorites_test.html', context)