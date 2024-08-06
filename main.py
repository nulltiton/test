from flask import Flask, render_template

app = Flask(__name__)

# Массив с координатами
coordinates = [
    {"id": 1, "latitude": 40.712776, "longitude": -74.005974, "description": "New York City, USA"},
    {"id": 2, "latitude": 34.052235, "longitude": -118.243683, "description": "Los Angeles, USA"},
    {"id": 3, "latitude": 48.856613, "longitude": 2.352222, "description": "Paris, France"},
    {"id": 4, "latitude": 51.507351, "longitude": -0.127758, "description": "London, UK"},
    {"id": 5, "latitude": 35.689487, "longitude": 139.691711, "description": "Tokyo, Japan"},
    {"id": 6, "latitude": -33.868820, "longitude": 151.209290, "description": "Sydney, Australia"},
    {"id": 7, "latitude": 55.755825, "longitude": 37.617298, "description": "Moscow, Russia"},
    {"id": 8, "latitude": 39.904202, "longitude": 116.407394, "description": "Beijing, China"},
    {"id": 9, "latitude": -23.550520, "longitude": -46.633308, "description": "São Paulo, Brazil"},
    {"id": 10, "latitude": 19.432608, "longitude": -99.133209, "description": "Mexico City, Mexico"}
]


@app.route('/')
def index():
    return render_template('index.html', coordinates=coordinates)


if __name__ == '__main__':
    app.run(debug=True)
