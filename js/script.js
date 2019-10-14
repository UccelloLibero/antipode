//  button onclick="results()" function
function results() {

  // get input values and encode for querystring for the url in ajax request
  const latitudeValue = encodeURIComponent(document.getElementById('latitude').value);
  const longitudeValue = encodeURIComponent(document.getElementById('longitude').value);

  // begin new ajax request
  const request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      // parse JSON response from server
      const coords = JSON.parse(this.responseText);

      console.log(coords[0].latitude, coords[1].longitude);

      // select input fields to be polpulated by responseText values
      var antiLatitude = document.getElementById('latitude-result');
      antiLatitude.value = coords[0].latitude;
      var antiLongitude = document.getElementById('longitude-result');
      antiLongitude.value = coords[1].longitude;
    }
  };
// method 'GET', url with query string preconstructed and values captured above, true for asynchronous update of page content
request.open('GET', 'http://127.0.0.1:5000/antipode/?latitude='+latitudeValue+'&longitude='+longitudeValue, true);
request.send();


}

// initialize the map and set it's view to default geo coords - Atlanta - and set it's zoom level

// set map view to be ATL coords as default values and on calculate update the map view to the antipode coordinates -- learn how to use the ajax response outside of the function results()


var mymap = L.map('osmaps').setView([antiLatitude.value, antiLongitude.value], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoidWNjZWxsb2xpYmVybyIsImEiOiJjanl0NGZhdnIwMGFpM2ttZXNzY3Y4aWdpIn0.pceTn4SfqNTHcFxrprRUPw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'your.mapbox.access.token'
}).addTo(mymap);
