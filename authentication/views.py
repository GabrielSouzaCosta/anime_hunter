from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from animes.models import Favorite, Watchlist_item
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings    


def login_view(request):
    msg = ''
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data.get('username'), 
                password = form.cleaned_data.get('password')
                )
            if user is not None:
                login(request, user)
                return redirect('animes:homepage')
            else: 
                msg = "Wrong username or password"

    return render(request, 'authentication/login.html', {'form': form, 'msg': msg}) 

def logout_view(request):
    logout(request)
    return redirect('animes:homepage')

def register(request):
    msg = ''
    if request.method == 'POST':
        form = NewUserForm(data=request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('animes:homepage')
        msg = "Error"
    else:
        form = NewUserForm()
        
    return render(request, 'authentication/register.html', {'form': form, 'msg': msg})

def user_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    favorites = Favorite.objects.filter(user=request.user)
    watchlist_items = Watchlist_item.objects.filter(user=request.user)
    return render(request, 'authentication/user_list.html', {'favorites': favorites, 'watchlist_items': watchlist_items})