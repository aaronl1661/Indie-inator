from django import forms

from .models import Product, Username, Playlist, Song
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Your Title"}))
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        return title 

class UsernameForm(forms.ModelForm):
    class Meta:
        model = Username
        fields = [
            'username', 
        ]
    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        return username
    


class PlaylistForm(forms.Form):
    def __init__(self, username, *args, **kwargs):
        super(PlaylistForm, self).__init__(*args, **kwargs)
        a = forms.CharField(max_length=30)
        sp = spotipy.Spotify(client_credentials_manager= SpotifyClientCredentials(client_id='9ddfda6a0c7646de9ca807815a136349', client_secret='d8f8a4e0660c434e837cde60d0fdb526'))
        temp = sp.user_playlists(username)
        PLAYLIST_CHOICES = []
        for i in range(0, len(temp['items'])):
            temp_tuple = (temp['items'][i]['id'], temp['items'][i]['name'])
            PLAYLIST_CHOICES.append(temp_tuple)
        self.fields['playlist'] = forms.ChoiceField(choices=PLAYLIST_CHOICES)
class GenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("test" , 'test')
])
class AfroGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("afrobeat",    "afrobeat (Afro)"),
("blues",   "blues(Afro)"),
("dancehall",   "dancehall(Afro)"),
("funk",    "funk(Afro)"),
("reggae",  "reggae(Afro)"),
("reggaeton",   "reggaeton(Afro)"),
("soul",    "soul(Afro)"),
("ska", "ska(Afro)")
])
class AsianGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("anime",   "anime(Asian)"),
("cantopop",    "cantopop(Asian)"),
("indian",  "indian(Asian)"),
("j-dance", "j-dance(Asian)"),
("j-idol",  "j-idol(Asian)"),
("j-pop",   "j-pop(Asian)"),
("j-rock",  "j-rock(Asian)"),
("k-pop",   "k-pop(Asian)"),
("malay",   "malay(Asian)"),
("mandopop",    "mandopop(Asian)"),
("philippines-opm", "philippines-opm(Asian)")])
class CountryGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("bluegrass",   "bluegrass(Country)"),
("country", "country(Country)"),
("folk",    "folk(Country)"),
("honky-tonk",  "honky-tonk(Country)")])
class DanceGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("dance",   "dance(Dance)"),
("disco",   "disco(Dance)"),
("groove",  "groove(Dance)"),
("salsa",   "salsa(Dance)"),
("tango",   "tango(Dance)")])
class ElectronicGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("detroit-techno",  "detroit-techno(Electronic Music) "),
("drum-and-bass",   "drum-and-bass(Electronic Music) "),
("dub", "dub(Electronic Music) "),
("dubstep", "dubstep(Electronic Music) "),
("edm", "edm(Electronic Music) "),
("electro", "electro(Electronic Music) "),
("electronic",  "electronic(Electronic Music) "),
("grindcore",   "grindcore(Electronic Music) "),
("hardstyle",   "hardstyle(Electronic Music) "),
("idm", "idm(Electronic Music) "),
("industrial",  "industrial(Electronic Music) "),
("minimal-techno",  "minimal-techno(Electronic Music) "),
("post-dubstep",    "post-dubstep(Electronic Music) "),
("techno",  "techno(Electronic Music) "),
("trip-hop",    "trip-hop(Electronic Music) ")])
class HappyGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("road-trip",   "road-trip(Happy Vibey)"),
("summer",  "summer(Happy Vibey)"),
("happy",   "happy(Happy Vibey)")])
class HouseGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("house",   "house(House)"),
("garage",  "garage(House)"),
("breakbeat",   "breakbeat(House)"),
("progressive-house",   "progressive-house(House)")])
class IndieGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("indie",   "indie(Indie)"),
("indie-pop",   "indie-pop(Indie)")
])
class InstrumentalGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("ambient", "ambient(Instrumental)"),
("acoustic",   "acoustic(Instrumental)"),
("classical",   "classical(Instrumental)"),
("guitar",  "guitar(Instrumental)"),
("romance", "romance(Instrumental)")])
class PopGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("power-pop",   "power-pop(Pop)"),
("pop", "pop(Pop)"),
("pop-film",    "pop-film(Pop)"),
("party",   "party(Pop)")])
class RapGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("hip-hop", "hip-hop(Rap)")])
class RockGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("alt-rock",    "alt-rock(Rock)"),
("black-metal", "black-metal(Rock)"),
("death-metal", "death-meta(Rock)l"),
("emo", "emo(Rock)"),
("goth",    "goth(Rock)"),
("grunge",  "grunge(Rock)"),
("hard-rock",   "hard-rock(Rock)"),
("hardcore",    "hardcore(Rock)"),
("heavy-metal", "heavy-meta(Rock)l"),
("metal",   "metal(Rock)"),
("metal-misc",  "metal-misc(Rock)"),
("metalcore",   "metalcore(Rock)"),
("new-age", "new-age(Rock)"),
("psych-rock",  "psych-rock(Rock)"),
("punk",    "punk(Rock)"),
("punk-rock",   "punk-rock(Rock)"),
("rock",    "rock(Rock)"),
("rockabilly",  "rockabilly(Rock)"),
("rock-n-roll", "rock-n-roll(Rock)"),
("trance",  "trance(Rock)")])
class SlowGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("alternative", "alternative(Slow/Chill)"),
("chicago-house",   "chicago-house(Slow/Chill)"),
("club",    "club(Slow/Chill)"),
("chill",   "chill(Slow/Chill)"),
("deep-house",  "deep-house(Slow/Chill)"),
("jazz",    "jazz(Slow/Chill)"),
("piano",   "piano(Slow/Chill)"),
("rainy-day",   "rainy-day(Slow/Chill)"),
("r-n-b",   "r-n-b(Slow/Chill)"),
("sad", "sad(Slow/Chill)"),
("sleep",   "sleep(Slow/Chill)"),
("study",   "study(Slow/Chill)")])
class SoundtrackGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("disney",  "disney(Soundtrack)"),
("movies",  "movies(Soundtrack)"),
("show-tunes",  "show-tunes(Soundtrack)"),
("soundtracks", "soundtracks(Soundtrack)")])
class SouthAmericanGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("bossanova",   "bossanova(South American)"),
("brazil",  "brazil(South American)"),
("forro",   "forro(South American)"),
("latin",   "latin(South American)"),
("latino",  "latino(South American)"),
("mpb", "mpb(South American)"),
("pagode",  "pagode(South American)"),
("samba",   "samba(South American)"),
("sertanejo",   "sertanejo(South American)"),
("spanish", "spanish(South American)")])
class WorldGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("british", "british(World Music)"),
("french",  "french(World Music)"),
("german",  "german(World Music)"),
("iranian", "iranian(World Music)"),
("swedish", "swedish(World Music)"),
("turkish", "turkish(World Music)"),
("world-music", "world-music(World Music)")])
class MiscGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("children",    "children(Misc)"),
("comedy",  "comedy(Misc)"),
("gospel",  "gospel(Misc)"),
("holidays",    "holidays(Misc)"),
("new-release", "new-release(Misc)"),
("opera",   "opera(Misc)"),
("singer-songwriter",   "singer-songwriter(Misc)"),
("songwriter",  "songwriter(Misc)"),
("synth-pop",   "synth-pop(Misc)")])    

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = [
            'song', 
        ]
class SongGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [])

   
class SongAfroGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("afrobeat",    "afrobeat (Afro)"),
("blues",   "blues(Afro)"),
("dancehall",   "dancehall(Afro)"),
("funk",    "funk(Afro)"),
("reggae",  "reggae(Afro)"),
("reggaeton",   "reggaeton(Afro)"),
("soul",    "soul(Afro)"),
("ska", "ska(Afro)")
])
class SongAsianGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("anime",   "anime(Asian)"),
("cantopop",    "cantopop(Asian)"),
("indian",  "indian(Asian)"),
("j-dance", "j-dance(Asian)"),
("j-idol",  "j-idol(Asian)"),
("j-pop",   "j-pop(Asian)"),
("j-rock",  "j-rock(Asian)"),
("k-pop",   "k-pop(Asian)"),
("malay",   "malay(Asian)"),
("mandopop",    "mandopop(Asian)"),
("philippines-opm", "philippines-opm(Asian)")])
class SongCountryGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("bluegrass",   "bluegrass(Country)"),
("country", "country(Country)"),
("folk",    "folk(Country)"),
("honky-tonk",  "honky-tonk(Country)")])
class SongDanceGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("dance",   "dance(Dance)"),
("disco",   "disco(Dance)"),
("groove",  "groove(Dance)"),
("salsa",   "salsa(Dance)"),
("tango",   "tango(Dance)")])
class SongElectronicGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("detroit-techno",  "detroit-techno(Electronic Music) "),
("drum-and-bass",   "drum-and-bass(Electronic Music) "),
("dub", "dub(Electronic Music) "),
("dubstep", "dubstep(Electronic Music) "),
("edm", "edm(Electronic Music) "),
("electro", "electro(Electronic Music) "),
("electronic",  "electronic(Electronic Music) "),
("grindcore",   "grindcore(Electronic Music) "),
("hardstyle",   "hardstyle(Electronic Music) "),
("idm", "idm(Electronic Music) "),
("industrial",  "industrial(Electronic Music) "),
("minimal-techno",  "minimal-techno(Electronic Music) "),
("post-dubstep",    "post-dubstep(Electronic Music) "),
("techno",  "techno(Electronic Music) "),
("trip-hop",    "trip-hop(Electronic Music) ")])
class SongHappyGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("road-trip",   "road-trip(Happy Vibey)"),
("summer",  "summer(Happy Vibey)"),
("happy",   "happy(Happy Vibey)")])
class SongHouseGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("house",   "house(House)"),
("garage",  "garage(House)"),
("breakbeat",   "breakbeat(House)"),
("progressive-house",   "progressive-house(House)")])
class SongIndieGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("indie",   "indie(Indie)"),
("indie-pop",   "indie-pop(Indie)")
])
class SongInstrumentalGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("ambient", "ambient(Instrumental)"),
("acoustic",   "acoustic(Instrumental)"),
("classical",   "classical(Instrumental)"),
("guitar",  "guitar(Instrumental)"),
("romance", "romance(Instrumental)")])
class SongPopGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("power-pop",   "power-pop(Pop)"),
("pop", "pop(Pop)"),
("pop-film",    "pop-film(Pop)"),
("party",   "party(Pop)")])
class SongRapGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("hip-hop", "hip-hop(Rap)")])
class SongRockGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("alt-rock",    "alt-rock(Rock)"),
("black-metal", "black-metal(Rock)"),
("death-metal", "death-meta(Rock)l"),
("emo", "emo(Rock)"),
("goth",    "goth(Rock)"),
("grunge",  "grunge(Rock)"),
("hard-rock",   "hard-rock(Rock)"),
("hardcore",    "hardcore(Rock)"),
("heavy-metal", "heavy-meta(Rock)l"),
("metal",   "metal(Rock)"),
("metal-misc",  "metal-misc(Rock)"),
("metalcore",   "metalcore(Rock)"),
("new-age", "new-age(Rock)"),
("psych-rock",  "psych-rock(Rock)"),
("punk",    "punk(Rock)"),
("punk-rock",   "punk-rock(Rock)"),
("rock",    "rock(Rock)"),
("rockabilly",  "rockabilly(Rock)"),
("rock-n-roll", "rock-n-roll(Rock)"),
("trance",  "trance(Rock)")])
class SongSlowGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("alternative", "alternative(Slow/Chill)"),
("chicago-house",   "chicago-house(Slow/Chill)"),
("club",    "club(Slow/Chill)"),
("chill",   "chill(Slow/Chill)"),
("deep-house",  "deep-house(Slow/Chill)"),
("jazz",    "jazz(Slow/Chill)"),
("piano",   "piano(Slow/Chill)"),
("rainy-day",   "rainy-day(Slow/Chill)"),
("r-n-b",   "r-n-b(Slow/Chill)"),
("sad", "sad(Slow/Chill)"),
("sleep",   "sleep(Slow/Chill)"),
("study",   "study(Slow/Chill)")])
class SongSoundtrackGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("disney",  "disney(Soundtrack)"),
("movies",  "movies(Soundtrack)"),
("show-tunes",  "show-tunes(Soundtrack)"),
("soundtracks", "soundtracks(Soundtrack)")])
class SongSouthAmericanGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("bossanova",   "bossanova(South American)"),
("brazil",  "brazil(South American)"),
("forro",   "forro(South American)"),
("latin",   "latin(South American)"),
("latino",  "latino(South American)"),
("mpb", "mpb(South American)"),
("pagode",  "pagode(South American)"),
("samba",   "samba(South American)"),
("sertanejo",   "sertanejo(South American)"),
("spanish", "spanish(South American)")])
class SongWorldGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("british", "british(World Music)"),
("french",  "french(World Music)"),
("german",  "german(World Music)"),
("iranian", "iranian(World Music)"),
("swedish", "swedish(World Music)"),
("turkish", "turkish(World Music)"),
("world-music", "world-music(World Music)")])
class SongMiscGenreForm(forms.Form):
    genre = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices= [("children",    "children(Misc)"),
("comedy",  "comedy(Misc)"),
("gospel",  "gospel(Misc)"),
("holidays",    "holidays(Misc)"),
("new-release", "new-release(Misc)"),
("opera",   "opera(Misc)"),
("singer-songwriter",   "singer-songwriter(Misc)"),
("songwriter",  "songwriter(Misc)"),
("synth-pop",   "synth-pop(Misc)")])

class RawProductForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
                                                    "placeholder" : "Your Title"
                                                    }
                                                )
                                            )
    description = forms.CharField()
    price = forms.DecimalField()