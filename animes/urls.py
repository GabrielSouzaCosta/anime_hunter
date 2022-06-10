from django.urls import path
from . import views

app_name = 'animes'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search_results/', views.search_animes_view, name='search_animes'),
    path('animes/<int:id>/', views.anime_details, name='anime_details'),
    path('top/', views.top_animes, name='top_animes'), 
    path('upcoming/', views.upcoming_animes, name='upcoming_animes'),
    path('discover/', views.discover, name="discover"),
    path('add_favorite/<int:anime_id>/', views.add_favorite, name='add_favorite'),
    path('add_to_watchlist/<int:anime_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('remove_favorite/<int:anime_id>/', views.remove_favorite, name='remove_favorite'),
    path('remove_from_watchlist/<int:anime_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),
    path('set_episodes/<int:anime_id>/', views.set_episodes, name='set_episodes'),
]
 