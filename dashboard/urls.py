
from unicodedata import name
from django.urls import path, include
from .views import cards, dashboard, logout_view, userinterface, songs, artists, hashtags,listartistsongs

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('logout/', logout_view, name='adminlogout'),
    path('userinterface/', userinterface, name='userinterface'),
    path('songs/', songs, name='songs'),
    path('artists/', artists, name='artists'),
    path('hashtags/', hashtags, name='hashtags'),
    path('cards/', cards, name='cards'),
    path('display/', cards, name='cards'),

    
]
