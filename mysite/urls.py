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
from products.views import product_create_view, username_view, playlist_view, genre_view, final_song_selection_view, song_view, song_confirm_view ,song_genre_view, song_rec_view

urlpatterns = [
    path('', home_view),
    path('home/', home_view),
    path('playlist1/', username_view),
    path('playlist2/', playlist_view),
    path('playlist3/', genre_view),
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