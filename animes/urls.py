from django.urls import path
from . import views

app_name = 'animes'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('search_results/', views.search_animes_view, name='search_animes'),
    path('animes/<int:id>/', views.anime_details, name='anime_details'),
    path('top/', views.top_animes, name='top_animes'), 
    path('upcoming/', views.upcoming_animes, name='upcoming_animes')
]
 