from jikanpy import AioJikan, Jikan
from pprint import pprint
import requests

jikan = Jikan(selected_base='https://api.jikan.moe/v4')

def get_anime(id):
    return jikan.anime(id)

async def search_anime(query):
    async with AioJikan() as aio_jikan:
        try:
            search = await aio_jikan.search(search_type='anime', page=1, query=query)
        except:
            return False
    return search['results']
    
def get_top_animes():
    return jikan.top(type='anime')['data']

def get_upcoming_animes():
    response = requests.get('https://api.jikan.moe/v4/top/anime?filter=upcoming').json()
    return response['data']


