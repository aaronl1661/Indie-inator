from django.contrib import admin

# Register your models here.
from . models import Product, Username, Playlist, Song

admin.site.register(Product)
admin.site.register(Username)
admin.site.register(Playlist)
admin.site.register(Song)