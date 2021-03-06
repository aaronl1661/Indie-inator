from django.shortcuts import render, redirect

from . forms import ProductForm, RawProductForm, UsernameForm, PlaylistForm, GenreForm, SongForm, SongGenreForm , AfroGenreForm, AsianGenreForm, CountryGenreForm, DanceGenreForm, ElectronicGenreForm, HappyGenreForm, HouseGenreForm, IndieGenreForm,InstrumentalGenreForm,PopGenreForm,RapGenreForm,RockGenreForm,SlowGenreForm,SoundtrackGenreForm,SouthAmericanGenreForm,WorldGenreForm,MiscGenreForm,\
    SongAfroGenreForm, SongAsianGenreForm, SongCountryGenreForm, SongDanceGenreForm, SongElectronicGenreForm, SongHappyGenreForm, SongHouseGenreForm, SongIndieGenreForm, SongInstrumentalGenreForm, SongPopGenreForm, SongRapGenreForm, SongRockGenreForm, SongSlowGenreForm, SongSoundtrackGenreForm, SongSouthAmericanGenreForm, SongWorldGenreForm, SongMiscGenreForm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from . models import Product, Username, Playlist
from django import forms
import csv
#from scripts.script import run, init_sp, get_id_list,create_playlist,create_playlist_df, get_centroid, get_final_songs
import celery
from django.contrib import messages
from .tasks import run
from time import sleep
import json
from celery.result import AsyncResult
# Create your views here.

def product_create_view(request):
    initial_data = {
        'title' : "My Title"
    }
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
        data = request.POST.dict()
        print(data)
        with open('data.csv', 'w') as f:
            for key in data.keys():
                f.write("%s,%s\n"%(key,data[key]))
                print(data[key])

    context = {
        'form' : form 
    }
    
    return render(request, "product_create.html", context)

def username_view(request):
    sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526', requests_timeout=100))
    form = UsernameForm(request.POST or None)
    
    if form.is_valid():
        try:
            r = sp.user_playlists(request.POST.get('username' , '').strip())
            form.save()
            #form = UsernameForm()
            data = request.POST.get('username', '').strip()
            request.session['username'] = data
            context = {
            'form' : form, 
            'username' : data
            }
            return redirect('/playlist2/')
        except spotipy.exceptions.SpotifyException as e:  # This is the correct syntax
            form = UsernameForm() 
            messages.error(request, "Not a valid Username")

        
    context = {
        'form':form,
    }
    return render(request, "playlist1.html", context)
        

def playlist_view(request):
    form = PlaylistForm(request.session['username'])
    if request.POST:
        #form.save()
        #print('entered')
        #form = PlaylistForm(request.session['username'])
        
        data = request.POST.get('playlist')
        request.session['playlist_choice'] = data
        print(data)
        return redirect('/playlist3/')
    context = {
            'form' : form
        }
    return render(request, "playlist2.html", context)

def genre_view(request):
    form = GenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5:
        print("print entered")
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        print(data)

        return redirect('/playlist4/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = GenreForm()
    context = {
            'form' : form
        }
    return render(request, "playlist3.html", context)

def waiting_view(request):
    print('entered waiting view')
    playlist = request.session['playlist_choice']
    genre = request.session['genre_choice']
    print('playlist genre recieved')
    async_result = run.delay(playlist, genre)
    print('async created')
    request.session['task_id'] = async_result.task_id
    print('request session recieved')
    #return redirect('/playlist4/')
    return render(request, 'playlistwaiting.html')


def final_song_selection_view(request):

    context = {'data' : AsyncResult(request.session['task_id']).get()}
    return(render(request, 'playlist4.html', context))


def afro_genre_view(request):
    form = AfroGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        print(data)
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = AfroGenreForm()
    context = {
            'form' : form
        }
    return render(request, "afro_p.html", context)
def asian_genre_view(request):
    form = AsianGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = AsianGenreForm()
    context = {
            'form' : form
        }
    return render(request, "asian_p.html", context)
def country_genre_view(request):
    form = CountryGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = CountryGenreForm()
    context = {
            'form' : form
        }
    return render(request, "country_p.html", context)
def dance_genre_view(request):
    form = DanceGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = GenreForm()
    context = {
            'form' : form
        }
    return render(request, "dance_p.html", context)    
def electronic_genre_view(request):
    form = ElectronicGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = ElectronicGenreForm()
    context = {
            'form' : form
        }
    return render(request, "electronic_p.html", context)    
def happy_genre_view(request):
    form = HappyGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        print(data)
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = HappyGenreForm()
    context = {
            'form' : form
        }
    return render(request, "happy_p.html", context)    
def house_genre_view(request):
    form = HouseGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = HouseGenreForm()
    context = {
            'form' : form
        }
    return render(request, "house_p.html", context)    
def indie_genre_view(request):
    form = IndieGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = IndieGenreForm()
    context = {
            'form' : form
        }
    return render(request, "indie_p.html", context)    
def instrumental_genre_view(request):
    form = InstrumentalGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = InstrumentalGenreForm()
    context = {
            'form' : form
        }
    return render(request, "instrumental_p.html", context)    
def pop_genre_view(request):
    form = PopGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = PopGenreForm()
    context = {
            'form' : form
        }
    return render(request, "pop_p.html", context)    
def rap_genre_view(request):
    form = RapGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = RapGenreForm()
    context = {
            'form' : form
        }
    return render(request, "rap_p.html", context)    
def rock_genre_view(request):
    form = RockGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = RockGenreForm()
    context = {
            'form' : form
        }
    return render(request, "rock_p.html", context)    
def slow_genre_view(request):
    form = SlowGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SlowGenreForm()
    context = {
            'form' : form
        }
    return render(request, "slow_p.html", context)    
def soundtrack_genre_view(request):
    form = SoundtrackGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SoundtrackGenreForm()
    context = {
            'form' : form
        }
    return render(request, "soundtrack_p.html", context)    
def south_american_genre_view(request):
    form = SouthAmericanGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SouthAmericanGenreForm()
    context = {
            'form' : form
        }
    return render(request, "southamerican_p.html", context)    
def world_genre_view(request):
    form = WorldGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5: 
            form = WorldGenreForm()
    context = {
            'form' : form
        }
    return render(request, "worldmusic_p.html", context)    
def misc_genre_view(request):
    form = MiscGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = MiscGenreForm()
    context = {
            'form' : form
        }
    return render(request, "misc_p.html", context)    


#Start of song genres
#
#

def song_afro_genre_view(request):
    form = SongAfroGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongAfroGenreForm()
    context = {
            'form' : form
        }
    return render(request, "afro_s.html", context)
def song_asian_genre_view(request):
    form = SongAsianGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongAsianGenreForm()
    context = {
            'form' : form
        }
    return render(request, "asian_s.html", context)
def song_country_genre_view(request):
    form = SongCountryGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongCountryGenreForm()
    context = {
            'form' : form
        }
    return render(request, "country_s.html", context)
def song_dance_genre_view(request):
    form = SongDanceGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongGenreForm()
    context = {
            'form' : form
        }
    return render(request, "dance_s.html", context)    
def song_electronic_genre_view(request):
    form = SongElectronicGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongElectronicGenreForm()
    context = {
            'form' : form
        }
    return render(request, "electronic_s.html", context)    
def song_happy_genre_view(request):
    form = SongHappyGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongHappyGenreForm()
    context = {
            'form' : form
        }
    return render(request, "happy_s.html", context)    
def song_house_genre_view(request):
    form = SongHouseGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongHouseGenreForm()
    context = {
            'form' : form
        }
    return render(request, "house_s.html", context)    
def song_indie_genre_view(request):
    form = SongIndieGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongIndieGenreForm()
    context = {
            'form' : form
        }
    return render(request, "indie_s.html", context)    
def song_instrumental_genre_view(request):
    form = SongInstrumentalGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongInstrumentalGenreForm()
    context = {
            'form' : form
        }
    return render(request, "instrumental_s.html", context)    
def song_pop_genre_view(request):
    form = SongPopGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongPopGenreForm()
    context = {
            'form' : form
        }
    return render(request, "pop_s.html", context)    
def song_rap_genre_view(request):
    form = SongRapGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongRapGenreForm()
    context = {
            'form' : form
        }
    return render(request, "rap_s.html", context)    
def song_rock_genre_view(request):
    form = SongRockGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongRockGenreForm()
    context = {
            'form' : form
        }
    return render(request, "rock_s.html", context)    
def song_slow_genre_view(request):
    form = SongSlowGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongSlowGenreForm()
    context = {
            'form' : form
        }
    return render(request, "slow_s.html", context)    
def song_soundtrack_genre_view(request):
    form = SongSoundtrackGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongSoundtrackGenreForm()
    context = {
            'form' : form
        }
    return render(request, "soundtrack_s.html", context)    
def song_south_american_genre_view(request):
    form = SongSouthAmericanGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongSouthAmericanGenreForm()
    context = {
            'form' : form
        }
    return render(request, "southamerican_s.html", context)    
def song_world_genre_view(request):
    form = SongWorldGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5: 
            form = SongWorldGenreForm()
    context = {
            'form' : form
        }
    return render(request, "worldmusic_s.html", context)    
def song_misc_genre_view(request):
    form = SongMiscGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5 and len(request.POST.getlist('genre')) != 0:
        data = request.POST.getlist('genre')
        request.session['genre_choice'] = data
        return redirect('/waitingp/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongMiscGenreForm()
    context = {
            'form' : form
        }
    return render(request, "misc_s.html", context)      


def song_view(request):
    sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526', requests_timeout=100))
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SongForm()
        data = request.POST.get('song', '')
        #print(data)
        request.session['song'] = data
        context = {
            'form' : form, 
        }
        return redirect('/song2/')
    context = {
        'form':form,
    }
    return render(request, "song1.html", context)
def song_confirm_view(request, *args, **kwargs):
    sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526', requests_timeout=100))
    print(request.session['song'])
    id = sp.track(request.session['song'])['id']
    request.session['song_id'] = id
    data = "https://open.spotify.com/embed/track/" + id
    context = {
        'data' : data,
    }
    
    return render(request, "song2.html", context)  

def song_genre_view(request):
    form = SongGenreForm()
    if request.POST and len(request.POST.getlist('genre')) <= 5:
        print("print entered")
        data = request.POST.getlist('genre')
        request.session['song_genre_choice'] = data
        print(data)

        return redirect('/song4/')
    elif request.POST and len(request.POST.getlist('genre')) > 5:
        form = SongGenreForm()
    context = {
            'form' : form
        }
    return render(request, "song3.html", context)
  
def song_rec_view(request):
    sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526', requests_timeout=100))
    features = sp.audio_features(request.session['song_id'])[0]
    features_list = []
    for key in features:
        features_list.append(features[key])
    recommended_id = []
    new_recommended = []
    count = 0
    m = 0
    counter = 0    
    while len(new_recommended) < 1:
            recommended_id.clear()
            recommend = sp.recommendations(seed_genres=request.session['song_genre_choice'], target_danceability=features_list[0], target_energy=features_list[1], target_key=features_list[2], target_loudness=features_list[3], target_mode=features_list[4], target_speechiness=features_list[5] ,target_acousticness=features_list[6], target_instrumentalness=features_list[7],target_liveness=features_list[8], target_valence=features_list[9], target_tempo=features_list[10], target_time_signature=features_list[17], target_popularity=50, limit = 100)['tracks']
            temp_recommended = []
            for j in range(0, len(recommend)):
                    recommended_id.append(recommend[j]['id'])
            count = 0
            print(len(recommended_id))
            for id in recommended_id:
                    for i in range(0, len(sp.track(id)['artists'])):
                            if sp.artist(sp.track(id)['artists'][i]['id'])['popularity'] < 60: 
                                    #if int(sp.track(id)['album']['release_date'][0:4]) - 2016 > 0:
                                        temp_recommended.append(recommended_id[count])
                                        break
                    count += 1
            
            new_recommended.extend(temp_recommended)
            temp_recommended.clear()
            if counter != 0:
                    m= m*-1
            if counter % 2 == 0:
                    m+=.1

            print(len(new_recommended))
            counter+=1


    recommended_id.clear()
    recommended_id.extend(new_recommended)
    embedded_songs = []
    for id in recommended_id:
                embedded_songs.append("https://open.spotify.com/embed/track/" + id)    
    context = {
        "data" : embedded_songs
    }
    return(render(request, 'song4.html', context))





#def product_create_view(request):
#    my_form = RawProductForm()
#    if request.method == "POST":
#        my_form = RawProductForm(request.POST)
#        if my_form.is_valid():
#            #now the data is good
#            print(my_form.cleaned_data)
#            Product.objects.create(**my_form.cleaned_data)
#        else:
#            print(my_form.errors)
#    context = {
#        'form' : my_form
#    }
#    return render(request, "product_create.html", context)
    
