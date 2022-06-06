from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from animes.models import Favorite, Watchlist_item, Tierlist_rating
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
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

def register_user(request):
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

@login_required
def user_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
    watchlist_items = Watchlist_item.objects.filter(user=request.user)
    return render(request, 'authentication/user_list.html', {'watchlist_items': watchlist_items})

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user).order_by('last_change')
    tiers = Tierlist_rating.objects.filter(user=request.user)
    return render(request, 'authentication/favorites_list.html', {'favorites': favorites, 'tiers': tiers})

@login_required
def add_tier(request):
    if request.method == 'POST':
        tier = Tierlist_rating(tier = request.POST['tier'], user = request.user)
        tier.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def delete_tier(request, id):
    if request.method == 'POST':
        tier = Tierlist_rating.objects.get(pk=id)
        if tier:
            tier.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def define_tier(request):
    if request.method == 'POST':
        tier = Tierlist_rating.objects.get(pk = request.POST['tier-ids'])
        items = request.POST['ranked-items'].strip().split(' ')
        remove_items = request.POST['remove-items'].strip().split(' ')
        print(items, remove_items)
        if items != [""]:
            for item in items:
                obj = Favorite.objects.get(pk = int(item))
                obj.tier_rating = tier
                obj.save()
        if remove_items != [""]:
            for item in remove_items:
                obj = Favorite.objects.get(pk = int(item))
                obj.tier_rating = None
                obj.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

