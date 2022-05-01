from contextlib import redirect_stderr
import contextvars
from email.mime import image

from operator import add
from turtle import title
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import song
from .forms import addSongForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count

# Create your views here.
@login_required
@staff_member_required(login_url='adminlogin')
def addsong(response):
    if response.method == "POST":
        form = addSongForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            print("Data Saved")
            HttpResponseRedirect('/dashboard/')

    else:
        form = addSongForm()
    return render(response, "songs/addsong.html", {'form' : form})


def displaysong(response,songtitle):
     s= song.objects.get(title=songtitle)
     return render(response, "songs/displaysong.html", {"i":s})



@login_required
@staff_member_required(login_url='adminlogin')
def showSongs(response):
    s= song.objects.all()
    if response.method == "POST":
        s1 = response.POST.get("searchsong")
        s =  song.objects.filter(title=s1)
        s1 = response.POST.get("showdatabase")
    
    return render(response, "songs/showsongs.html", {"songs":s})




@login_required
@staff_member_required(login_url='adminlogin')
def showArtists(response):
    s= song.objects.all()
    result = (song.objects
    .values('artist')
    .annotate(dcounxt=Count('artist'))
    .order_by()
    )
   
    print(result)
    return render(response, "songs/showartists.html", {"result":s})





@login_required
@staff_member_required(login_url='adminlogin')
def deleterecord(response, id1):
    try:
       record = song.objects.get(id = id1)
       record.delete()
       # Showing message after deleting record
        
       return redirect('/dashboard/showsongs/')
    except song.DoesNotExist:
        record = None
   


'''create a edit form with'''
@login_required
# @staff_member_required(login_url='adminlogin')
def editrecord(response, id1):
    try:
        if response.method == "POST":
            print(response.POST)
            form = addSongForm(response.POST, response.FILES)
            if form.is_valid():
                record = song.objects.get(id = id1)
                record.title = response.POST.get('title')
                record.artist = response.POST.get('artist')
                record.genre = response.POST.get('genre')
                record.year = response.POST.get('year')
                record.save()
                return redirect('/dashboard/showsongs/')
        record = song.objects.get(id = id1)
        form = addSongForm(initial={'title': record.title, 'artist': record.artist, 'image': record.image, 'song': record.song})
        return render(response, "songs/editrecord.html", {"form":form, "record":record})
    except song.DoesNotExist:
        record = None



