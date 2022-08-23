import json
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def find_location():
    uri = 'http://api.ipstack.com/check?access_key='
    key = '35c43096adc9416dab6bdd2d1ad53069'
    geolocationUri = uri + key
    response = requests.get(geolocationUri)
    response_json = json.loads(response.text)
    lat = response_json['latitude']
    long = response_json['longitude']
    city = response_json['city']
    txt = 'Hello Mudano! This application is running in {city}'
    return txt.format(city = city)

if __name__ == "__main__":
    app.run(debug=True)