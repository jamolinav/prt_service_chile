from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def geolocation(request):
    return render(request, 'leaflet/demo/index.html')