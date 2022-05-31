from jikanpy import AioJikan, Jikan

jikan = Jikan()

def get_anime(id):
    return jikan.anime(id)

async def search_anime(query):
    async with AioJikan() as aio_jikan:
        search = await aio_jikan.search(search_type='anime', page=1, query=query)
    return search['results']
    
def get_top_animes():
    return jikan.top(type='anime')['top']

def get_upcoming_animes():
    return jikan.top(type='anime', page=2, subtype='upcoming')['top']

