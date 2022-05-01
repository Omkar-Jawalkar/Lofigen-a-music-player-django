
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from songs.models import song
from django.db.models import Count


# Create your views here.

def logout_view(response):
    logout(response)
    return redirect('adminlogin')

@login_required 
@staff_member_required(login_url='adminlogin')
def dashboard(response):
    return render(response,"dashboard/dashboard.html",{})

def userinterface(response):
    return render(response,"dashboard/userinterface.html",{})

def songs(response):
    s = song.objects.all()
    return render(response,"dashboard/songs.html",{"songs": s})

def artists(response):
    result = (song.objects
    .values('artist')
    .annotate(dcounxt=Count('artist'))
    .order_by()
    )

    return render(response,"dashboard/artists.html",{"result":result})

def listartistsongs(response,artistname):
    s = song.objects.filter(artist=artistname)
    return render(response,"dashboard/showartistsonglist.html",{"songs": s})

def hashtags(response):
    return render(response,"dashboard/hashtags.html",{})

def cards(response):
    s1 = song.objects.all()
    return render(response,"dashboard/cards.html",{"songs1": s1})