from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from .views import addsong, deleterecord, displaysong, showArtists, showSongs, editrecord
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("dashboard/addsong/", addsong, name="addsong"),
    path("displaysong/<str:songtitle>/", displaysong, name="displaysong" ),
    path("dashboard/showsongs/", showSongs , name="showSongs" ),
    path("dashboard/showartists/", showArtists , name="showArtists" ),
    path("dashboard/showsongs/<int:id1>/delete", deleterecord, name="deleterecord"),
    path("dashboard/showsongs/<int:id1>/edit", editrecord, name="editrecord"),
    path("deleteartist/<int:id1>/", deleterecord, name="deleterecord"),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

