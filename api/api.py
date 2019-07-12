import flask
from flask import request, current_app, make_response
from flask import render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return 'hello world'


# http://antipode/location?longitude=33.7679192&latitude=84.5606917

@app.route('/antipode/', methods=['GET', 'OPTIONS'])
def antipode():
    if request.method == 'OPTIONS':
        response = current_app.make_default_options_response()
        return response
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    response = flask.jsonify({'latitude':latitude},{'longitude':longitude})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    # '''<h1>The coords values are: {}, {}</h1>'''.format(latitude, longitude)

if __name__ == '__main__':
    app.run()
