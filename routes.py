from flask import Flask, render_template
from models import db, WeatherData
from config import Config
from etl import perform_etl

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/weather_data', methods=['GET'])
def display_weather_data():
    perform_etl()
    weather_data = WeatherData.query.all()
    return render_template('weather_data.html', weather_data=weather_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
