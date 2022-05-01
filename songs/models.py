from cProfile import label
from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.
class song(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    image = models.ImageField(upload_to="upload/") 
    song = models.FileField(null=True, upload_to="upload/")

    def __str__(self):
        return self.title
