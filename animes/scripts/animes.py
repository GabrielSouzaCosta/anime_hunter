from jikanpy import AioJikan, Jikan
from random import choice, randint
from pprint import pprint
import requests

categories = ["airing", "upcoming", "bypopularity", "favorite"]

jikan = Jikan(selected_base='https://api.jikan.moe/v4')

def get_anime(id):
    return jikan.anime(id)

def search_anime(query, page):
    response = requests.get(f"https://api.jikan.moe/v4/anime?q={query}&page={page}&limit=18&genres_exclude=12").json()
    return response
    
def get_top_animes(page):
    response = requests.get(f'https://api.jikan.moe/v4/top/anime?filter=rank&page={page}&limit=24').json()
    return response

def get_upcoming_animes(page):
    response = requests.get(f'https://api.jikan.moe/v4/top/anime?filter=upcoming&page={page}&limit=24').json()
    return response

def get_random_animes():
    response = requests.get(f'https://api.jikan.moe/v4/top/anime?filter={choice(categories)}&page={randint(1, 4)}').json()
    return response['data']

