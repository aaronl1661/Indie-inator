from django.db import models
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Create your models here.
class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default = 'this is cool')

class Username(models.Model):
    username = models.CharField(max_length=30)

class Playlist(models.Model):
    playlist = models.CharField(max_length=30)
class Song(models.Model):
    song = models.CharField(max_length=40)
