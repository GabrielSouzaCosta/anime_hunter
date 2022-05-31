from django.urls import path
from . import views

app_name = "authentication"


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('my_list', views.user_list, name='user_list'),
]
