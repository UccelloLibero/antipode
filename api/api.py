import flask
from flask import request, current_app, make_response
from flask import render_template

# The flask request object (from flask import request) contains data that the browser sends to this app (the url parameters)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return 'hello world'


# http://antipode/location?longitude=33.7679192&latitude=84.5606917
def antipode_coords(latitude, longitude):
  anti_l = 0.0
  anti_long = 0.0
  if latitude <= 90 or latitude > 0:
    anti_l = latitude * -1

  if longitude < 0:
    anti_long = longitude + 180
  elif longitude > 0:
    anti_long = longitude -180
  else:
    print('Something is not right.')

  return float(anti_l), float(anti_long)


@app.route('/antipode/', methods=['GET', 'OPTIONS'])
def antipode():
    if request.method == 'OPTIONS':
        response = current_app.make_default_options_response()
        return response
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    anti_lat, anti_long = antipode_coords(float(latitude), float(longitude))
    response = flask.jsonify({'latitude':anti_lat},{'longitude':anti_long})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    # '''<h1>The coords values are: {}, {}</h1>'''.format(latitude, longitude)

if __name__ == '__main__':
    app.run()
