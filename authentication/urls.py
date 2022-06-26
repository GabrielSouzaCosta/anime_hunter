from django.urls import path
from . import views

app_name = "authentication"


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register'),
    path('my_list', views.user_list, name='user_list'),
    path('favorites/', views.favorites_list, name='favorites_list'),
    path('add_tier/', views.add_tier, name='add_tier'),
    path('delete_tier/<int:id>/', views.delete_tier, name='delete_tier'),
    path('define_tier/', views.define_tier, name='define_tier'),
]
