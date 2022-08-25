import json
import requests
from flask import Flask

app = Flask(__name__)

def geolocate(args):
    uri = 'http://api.ipstack.com/check?access_key='
    key = '35c43096adc9416dab6bdd2d1ad53069'
    geolocationUri = uri + key
    response = requests.get(geolocationUri)
    response_json = json.loads(response.text)
    lat = response_json['latitude']
    long = response_json['longitude']
    city = response_json['city']
    txt = 'Hello Mudano! This application is running in {city}'
    txt = txt.format(city = city)
    print(txt)
    return txt

@app.before_first_request(geolocate)
@app.route('/')
def show_location():
    return geolocate()

if __name__ == "__main__":
    app.run(debug=True)