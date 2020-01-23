var antiLatitude;
var antiLongitude;

//  button onclick="results()" function
document.getElementById('calculate').onclick = function() {

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


var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 33.749099, lng: -84.390185},
    zoom: 8
  });
}
