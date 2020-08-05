from django.http import HttpResponse
from django.shortcuts import render 
from django.views.generic.list import ListView
import hitcount # import entire package
from hitcount.views import HitCountMixin
from .models import IP

# Create your views here.
def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except: 
        ip = ''
    return(ip)
def home_view(request, *args, **kwargs):
    print(get_ip(request))
    form = IP()
    form.ip = get_ip(request)
    form.save()
    return render( request, 'home.html', locals() )

#def playlist1_view(request, *args, **kwargs):
#    print(request.user)
#    return render(request, "playlist1.html", {})

def playlist2_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "playlist2.html", {})

def playlist3_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "playlist3.html", {})

def playlist4_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "playlist4.html", {})

def song1_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "song1.html", {})

def song2_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "song2.html", {})

def song3_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "song3.html", {})

def song4_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "song4.html", {})    

def donate_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "donate.html" , {})

def contact_view(*args, **kwargs):
    
    return HttpResponse("<h1>Contact pages </h1>")