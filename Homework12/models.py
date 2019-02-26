from app import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer, unique=True)
    city_name = db.Column(db.String, index=True)
    country = db.Column(db.String)
    lat = db.Column(db.Numeric)
    lng = db.Column(db.Numeric)

    def __init__(self, zip_code, city_name, country, lat, lng):
        self.zip_code = zip_code
        self.city_name = city_name
        self.country = country
        self.lat = lat
        self.lng = lng

    def __repr__(self):
        print('<City: {}, code: {}>'.format(self.city_name, self.zip_code))
