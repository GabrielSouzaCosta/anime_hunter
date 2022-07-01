from django.contrib import admin
from django.urls import path, include

handler404 = 'animes.views.handler404'

urlpatterns = [
    path('', include('animes.urls')),
    path('user/', include('authentication.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('verification/', include('verify_email.urls')),	
]
