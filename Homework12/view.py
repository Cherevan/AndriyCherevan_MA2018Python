from app import app, db
from flask import render_template, request
import requests

URL = 'https://maps.googleapis.com/maps/api/geocode/json'
KEY = 'AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show-list')
def show_cities():
    from models import City

    cities = City.query.all()

    return render_template('show_list.html', cities=cities)


@app.route('/delete')
def delete_city():
    from models import City

    cities = City.query.all()

    return render_template('delete.html', cities=cities)


@app.route('/delete-this', methods=['POST'])
def delete_this():
    from models import City

    post_code = request.form['post_code']

    city = City.query.filter_by(zip_code=post_code).first()

    if city is not None:
        db.session.delete(city)
        db.session.commit()

    cities = City.query.all()

    return render_template('delete.html', cities=cities)


@app.route('/show-city', methods=['POST'])
def show_city():
    from models import City

    cities_name = None
    country = None
    post_code = request.form['post_code']
    region = request.form['region']
    params = {
        'components': 'postal_code:{}'.format(post_code),
        'region': region,
        'key': KEY
    }

    city_by_code = City.query.filter_by(zip_code=post_code).first()
    if city_by_code is not None:
        return render_template('city_in_list.html', name=city_by_code.city_name)

    r = requests.get(URL, params=params)
    items = r.json()

    if items['status'] == 'ZERO_RESULTS':
        return render_template('incorrect.html', code=post_code)

    for row in items['results'][0]['address_components']:
        if row['types'][0] == 'locality':
            cities_name = row['long_name']
        elif row['types'][0] == 'country':
            country = row['long_name']

    lat = items['results'][0]['geometry']['location']['lat']
    lng = items['results'][0]['geometry']['location']['lng']

    city = City(zip_code=post_code, city_name=cities_name, country=country, lat=lat, lng=lng)
    db.session.add(city)
    db.session.commit()

    items = requests.get('https://en.wikipedia.org/api/rest_v1/page/media/' + cities_name).json()

    if len(items['items']) < 1:
        coat_of_arms = "default_coa.png"
    else:
        coat_of_arms = items['items'][2]['thumbnail']['source']

    return render_template('current_city.html', city=city, coa=coat_of_arms)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_404.html'), 404
