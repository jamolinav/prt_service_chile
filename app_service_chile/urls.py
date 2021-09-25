from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('gps', views.gps, name='gps'),
    path('geolocation', views.geolocation, name='geolocation'),
]
