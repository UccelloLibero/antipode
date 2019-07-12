// const button = document.getElementById('button');

var latitude = document.getElementById('latitude').value;
var longitude = document.getElementById('longitude').value;

button.addEventListener('click', calculate);

function calculate() {
  var request = new XMLHttpRequest();

  request.onreadystatechange = function() {
    if (request.readyState === 4 && request.status === 200) {
      alert(request.responseText);
    }
  };

  // ?latitude=84.5606917&longitude=33.7679192'
  request.open('GET', 'http://localhost:5000/antipode', true);
  request.send();

}
