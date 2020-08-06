"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pages.views import home_view, contact_view, song1_view, song2_view, song3_view, song4_view, donate_view
from products.views import product_create_view, username_view, playlist_view, genre_view, final_song_selection_view, song_view, song_confirm_view ,song_genre_view, song_rec_view, \
afro_genre_view, asian_genre_view, country_genre_view, dance_genre_view, electronic_genre_view, happy_genre_view, house_genre_view, indie_genre_view, instrumental_genre_view, pop_genre_view,\
rap_genre_view, rock_genre_view, slow_genre_view, soundtrack_genre_view, south_american_genre_view, world_genre_view, misc_genre_view

urlpatterns = [
    path('', home_view),
    path('home/', home_view),
    path('playlist1/', username_view),
    path('playlist2/', playlist_view),
    path('playlist3/', genre_view),
    path('afrop/', afro_genre_view),
    path('asianp/', asian_genre_view),
    path('countryp/', country_genre_view),
    path('dancep/', dance_genre_view),
    path('electronicp/', electronic_genre_view),
    path('happyp/', happy_genre_view),
    path('housep/', house_genre_view),
    path('indiep/', indie_genre_view),
    path('instrumentalp/', instrumental_genre_view),
    path('popp/', pop_genre_view),
    path('rapp/', rap_genre_view),
    path('rockp/', rock_genre_view),
    path('slowp/', slow_genre_view),
    path('soundtrackp/', soundtrack_genre_view),
    path('south_americanp/', south_american_genre_view),
    path('worldp/', world_genre_view),
    path('miscp/', misc_genre_view),
    path('playlist4/', final_song_selection_view),
    path('song1/', song_view),
    path('song2/', song_confirm_view),
    path('song3/', song_genre_view),
    path('song4/', song_rec_view),
    path('donate/', donate_view),
    path('contact/', contact_view),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('product/', product_create_view)
]

urlpatterns += staticfiles_urlpatterns()