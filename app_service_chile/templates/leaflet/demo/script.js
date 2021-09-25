var osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib='Map data © <a href="http://osm.org/copyright">OpenStreetMap</a> contributors';
var osm = new L.TileLayer(osmUrl, {
    attribution: osmAttrib,
    detectRetina: true
});

// please replace this with your own mapbox token!
var token = 'pk.eyJ1IjoiamFtb2xpbmF2IiwiYSI6ImNrdTA4Y3JidzNrd3UydnBtdDhpam0yaTQifQ._-wEf7pg6y7gEsMwDdefhQ';
var mapboxUrl = 'https://api.mapbox.com/styles/v1/mapbox/streets-v10/tiles/{z}/{x}/{y}@2x?access_token=' + token;
var mapboxAttrib = 'Map data © <a href="http://osm.org/copyright">OpenStreetMap</a> contributors. Tiles from <a href="https://www.mapbox.com">Mapbox</a>.';
var mapbox = new L.TileLayer(mapboxUrl, {
  //attribution: mapboxAttrib,
  tileSize: 512,
  zoomOffset: -1
});

var map = new L.Map('map', {
    tap: false, // ref https://github.com/Leaflet/Leaflet/issues/7255
    layers: [mapbox],
    //center: [-33.46254631098106, -70.65507286554855],
    zoom: 24,
    zoomControl: true
});

/*
L.marker([-33.46254631098106, -70.65507286554855]).addTo(map);
L.marker([-33.46254631098106, -71.65507286554855]).addTo(map);
L.marker([-33.46254631098106, -72.65507286554855]).addTo(map);
*/

// add location control to global name space for testing only
// on a production site, omit the "lc = "!
lc = L.control.locate({
    strings: {
        title: "Show me where I am, yo!"
    }
}).addTo(map);


// placeholders for the L.marker and L.circle representing user's current position and accuracy    
var current_position, current_accuracy;

function onLocationFound(e) {
  // if position defined, then remove the existing position marker and accuracy circle from the map
  if (current_position) {
      map.removeLayer(current_position);
      map.removeLayer(current_accuracy);
  }

  var radius = e.accuracy / 2;

  current_position = L.marker(e.latlng).addTo(map)
    .bindPopup("Te encuentras aproximadamente a un radio de " + radius + " metros de este punto!").openPopup();

  current_accuracy = L.circle(e.latlng, radius).addTo(map);
}

function onLocationError(e) {
  alert(e.message);
}

map.on('locationfound', onLocationFound);
map.on('locationerror', onLocationError);

// wrap map.locate in a function    
function locate() {
    map.locate({setView: true, maxZoom: 17});
    //alert('ok');
  }

// call locate every 3 seconds... forever
setInterval(locate, 600000);


L.Control.MyLocate = L.Control.Locate.extend({
    _drawMarker: function() {
      // override to customize the marker
    }
 });
 
 var lc = new L.Control.MyLocate();

 locate();