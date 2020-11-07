from celery import shared_task
from time import sleep
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import json
import csv
import numpy as np
import pandas as pd
import random
from statistics import stdev
def init_sp():
    sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526', requests_timeout=100))
    return sp

def get_id_list(playlist_id, sp):
    results = sp.playlist(playlist_id, fields="tracks, next")  
    tracks = results['tracks']
    id = []
    for item in tracks['items']:
            track = item['track']
            if track != None:
                if track['id'] != None:
                    id.append(track['id'])
    while tracks['next']:
        tracks = sp.next(tracks)
        for item in tracks['items']:
            track = item['track']
            if track != None:
                if track['id'] != None:
                    id.append(track['id'])
    return id

def create_playlist(playlist_id, sp):
    id_list = get_id_list(playlist_id, sp)
    split = int(len(id_list) / 100) + 1

    playlist_features = []
    for i in range(0, split):
        temp_list = id_list[i*99:(i+1)*99]
        playlist_features.extend(sp.audio_features(temp_list))

    df = pd.DataFrame.from_dict(playlist_features)
    del df['type']
    del df['id']
    del df['uri']
    del df['track_href']
    del df['analysis_url']

    df.loudness = df.loudness*(-1)
    return df

def create_playlist_df(playlist_id):
    sp = init_sp()
    return create_playlist(playlist_id,sp)
    
def get_centroid(dataset): #dataset is a dataframe
    result = [dataset['danceability'].sum() / len(dataset), dataset['energy'].sum() / len(dataset), dataset['key'].sum() / len(dataset), dataset['loudness'].sum() / len(dataset),dataset['mode'].sum() / len(dataset),dataset['speechiness'].sum() / len(dataset),dataset['acousticness'].sum() / len(dataset), dataset['instrumentalness'].sum() / len(dataset), dataset['liveness'].sum() / len(dataset), dataset['valence'].sum() / len(dataset), dataset['tempo'].sum() / len(dataset), dataset['duration_ms'].sum() / len(dataset), dataset['time_signature'].sum() / len(dataset)]
    return result

def get_final_songs(sp, df, result, final_genres): # result comes form get_centroid
        from statistics import stdev
        import spotipy
        if len(df.index) >= 2:
                sd_danceability = stdev(df.loc[0:,'danceability'])
                sd_energy = stdev(df.loc[0:,'energy'])
                sd_loudness = stdev(df.loc[0:,'loudness'])
                sd_speechiness = stdev(df.loc[0:,'speechiness'])
                sd_acousticness = stdev(df.loc[0:,'acousticness'])
                sd_instrumentalness = stdev(df.loc[0:,'instrumentalness'])
                sd_liveness = stdev(df.loc[0:,'liveness'])
                sd_valence = stdev(df.loc[0:,'valence'])
                sd_tempo = stdev(df.loc[0:,'tempo'])
                sd = [sd_danceability, sd_energy,  sd_loudness, sd_speechiness, sd_acousticness, sd_instrumentalness, sd_liveness, sd_valence, sd_tempo]
                largest = 0
                largest_index = 0
                for i, stdev in enumerate(sd,start =0):
                        if stdev > largest:
                                largest = stdev
                                largest_index = i

                m_danceability = 0
                m_energy = 0
                m_loudness = 0
                m_speechiness = 0
                m_acousticness = 0
                m_instrumentalness = 0
                m_liveness = 0
                m_valence = 0
                m_tempo = 0

                if largest_index==0:
                        m_danceability = 1
                elif largest_index==1:
                        m_energy = 1 
                elif largest_index==2:
                        m_loudness = 1
                elif largest_index==3:
                        m_speechiness = 1
                elif largest_index==4:
                        m_acousticness = 1
                elif largest_index==5:
                        m_instrumentalness = 1
                elif largest_index==6:
                        m_liveness = 1
                elif largest_index==7:
                        m_valence = 1
                elif largest_index==8:
                        m_tempo = 1
                        
                danceability = 0
                energy = 0
                key = 0
                loudness = 0
                mode = 0
                speechiness = 0
                acousticness = 0
                instrumentalness = 0
                liveness = 0
                valence = 0
                tempo = 0
                time_signature = 0

                danceability = result[0]
                energy = result[1]
                key = int(round(result[2]))
                loudness = result[3]
                mode = int(round(result[4]))
                speechiness = result[5]
                acousticness = result[6]
                instrumentalness = result[7]
                liveness = result[8]
                valence = result[9]
                tempo = result[10]
                time_signature = int(round(result[12]))
                #temp = [danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature]
                #print(temp)
                recommended_id = []
                new_recommended = []
                count = 0
                m = 0
                counter = 0
                while len(new_recommended) < 1:
                        recommended_id.clear()
                        recommend = sp.recommendations(seed_genres=final_genres, target_danceability=danceability + m*m_danceability, target_energy=energy + m*m_energy, target_key=key, target_loudness=loudness + m*m_loudness, target_mode=mode, target_speechiness=speechiness + m_speechiness ,target_acousticness=acousticness + m*m_acousticness, target_instrumentalness=instrumentalness + m_instrumentalness,target_liveness=liveness + m*m_liveness, target_valence=valence + m*m_valence, target_tempo=tempo + m*m_tempo, target_time_signature=time_signature, target_popularity=50, limit = 100)['tracks']
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
                return recommended_id
        elif len(df.index) < 2:
                sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526', requests_timeout=100))
                print('song_received')
                print(df.iloc[0].tolist())
                #features = sp.audio_features(df.iloc[0])
                features_list = df.iloc[0].tolist()

                recommended_id = []
                new_recommended = []
                count = 0
                m = 0
                counter = 0    
                while len(new_recommended) < 1:
                        recommended_id.clear()
                        recommend = sp.recommendations(seed_genres=final_genres, target_danceability=features_list[0], target_energy=features_list[1], target_key=int(features_list[2]), target_loudness=features_list[3], target_mode=int(features_list[4]), target_speechiness=features_list[5] ,target_acousticness=features_list[6], target_instrumentalness=features_list[7],target_liveness=features_list[8], target_valence=features_list[9], target_tempo=features_list[10], target_time_signature=int(features_list[12]), target_popularity=50, limit = 100)['tracks']
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
                return recommended_id
@shared_task(bind=True)
def run(self, playlist_id, final_genres):
        print('entered')
        sp = init_sp()
        print("sp created")
        df = create_playlist_df(playlist_id)
        print(type(df))
        result = get_centroid(df)
        print("created centroid")
        final_songs = get_final_songs(sp, df, result, final_genres)
        print("songs received")
        embedded_songs = []
        for id in final_songs:
                embedded_songs.append("https://open.spotify.com/embed/track/" + id)    
        return embedded_songs

# def run(self, playlist_id, final_genres):
#     script.run(playlist_id, final_genres)
#     return 'done'
