from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
import folium
import geocoder

# Create your views here.
def index(request):

    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    #m = folium.Map(location=[-33.462549, -70.655102], zoom_start=16)
    m = folium.Map(location=[-33.46222, -70.65518], zoom_start=16)

    icon_prt = folium.features.CustomIcon('http://127.0.0.1:5500/MyProjects/web-locator/prt.jpg', icon_size=(50, 50))
    icon_porche_naranjo = folium.features.CustomIcon('http://127.0.0.1:5500/MyProjects/web-locator/porche_rojo.png', icon_size=(50, 50))
    folium.Marker([-33.46011033534138, -70.65566059512977], tooltip='Click for more', icon=icon_prt, popup=country).add_to(m)

    folium.Marker([-33.46254631098106, -70.65507286554855], tooltip='Click for more', icon=icon_porche_naranjo, popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }

    return render(request, 'index.html', context)
