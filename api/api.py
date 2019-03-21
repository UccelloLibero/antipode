import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

thanks = [
    {
    'title': 'Thank you notes to Randall',
    'author': 'Maya Husic soon to be officaly MRS McPherson, proudly',
    'text': 'Dear Randall thank you for your kindness every day.',
    'year_published': '2019'
    },
    {
    'title': 'I Love You Randall',
    'author': 'Maya Husic soon to be officaly MRS McPherson, proudly',
    'text': 'I fucking adore you, Randall',
    'year_published': '2019'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '''<h1>AntiPode API</h1>
    <p>This site is a prototype for AntiPode API</p>'''


@app.route('/api/antipode/resources/thanks/all', methods=['GET'])
def api_all():
    return jsonify(thanks)

# http://antipode/location?longitude=33.7679192&latitude=84.5606917

@app.route('/antipode', methods=['GET'])
def antipode():
    longitude = request.args.get('longitude')
    return longitude


app.run()
