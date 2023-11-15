import requests
from models import db, WeatherData
from config import Config

def perform_etl():
    cities = ['São Paulo', 'Paris', 'Copenhague', 'Viena', 'Melbourne']
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.OPENWEATHER_API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_entry = WeatherData(
                city=city,
                temperature=data['main']['temp'],
                humidity=data['main']['humidity']
            )
            db.session.add(weather_entry)
            db.session.commit()
        else:
            print(f'Erro na extração dos dados para {city}')


