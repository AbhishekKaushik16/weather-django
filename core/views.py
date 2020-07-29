from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import Location
from .models import Locations
import requests
# Create your views here.

base = 'http://api.openweathermap.org/data/2.5/'
api_key = '18c576b922aa4a57701b077cdd3a4b17'

def index(response):
    if response.method == "POST":
        form = Location(response.POST or None)
        if form.is_valid():
            location = form.cleaned_data['location']
            new_location = Locations(location=location)
            new_location.save()

    all_weather = []
    for loc in Locations.objects.all():
        resp = requests.get(base+'weather?q='+loc.location+'&units=metric&APPID='+api_key).json()
        weather = {
            'city': loc.location,
            'temp': resp['main']['temp'],
            'description': resp['weather'][0]['description'],
            'icon': resp['weather'][0]['icon']
        }
        all_weather.append(weather)
    context = {
        'form': Location(),
        'weather': all_weather
    }
    return render(response, "index.html",context)
    