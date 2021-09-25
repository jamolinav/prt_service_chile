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
    m = folium.Map(location=[-33.46011033534138, -70.65566059512977], zoom_start=16)

    icon_prt = folium.features.CustomIcon('app_service_chile/static/imgs/prt.jpg', icon_size=(50, 50))
    icon_porche_naranjo = folium.features.CustomIcon('app_service_chile/static/imgs/porche_rojo.png', icon_size=(50, 50))
    #folium.Marker([-33.46011033534138, -70.65566059512977], tooltip='Click for more', icon=icon_prt, popup=country).add_to(m)

    folium.Marker([-33.46011033534138, -70.65566059512977], tooltip='Click for more', icon=icon_porche_naranjo, popup=country).add_to(m)
    #folium.Marker([-33.46254631098106, -70.65507286554855], tooltip='Click for more', icon=icon_porche_naranjo, popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
    }

    return render(request, 'index.html', context)

def gps(request):
    print('GPS post')
    print(request.POST)

    lat = request.POST['latitude']
    lng =  request.POST['longitude']

    lat = -36.6330069
    lng = -72.9563881

    m = folium.Map(location=[lat, lng], zoom_start=16)

    icon_porche_naranjo = folium.features.CustomIcon('app_service_chile/static/imgs/porche_rojo.png', icon_size=(50, 50))

    folium.Marker([lat, lng], tooltip='Click for more', icon=icon_porche_naranjo).add_to(m)
    m = m._repr_html_()

    context = {
        'm': m,
    }
    print('render')
    return render(request, 'index.html', context)

def geolocation(request):
    return render(request, 'leaflet-locatecontrol/demo/index.html')