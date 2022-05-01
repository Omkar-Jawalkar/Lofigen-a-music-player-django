from csv import field_size_limit
from dataclasses import field, fields
from msilib.schema import Class
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import song

class addSongForm(forms.ModelForm):
    class Meta:
        model = song
        fields = ['title', 'artist', 'image', 'song']
        labels = {
                'title': _(''),
                'artist': _(''),
                'image': _(''),
                'song': _(''),
            }