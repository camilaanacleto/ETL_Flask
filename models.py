from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

db = SQLAlchemy()
brasil_timezone = pytz.timezone('America/Sao_Paulo')

def get_brasil_datetime():
    return datetime.now(brasil_timezone)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingestion_date = db.Column(db.DateTime, default=get_brasil_datetime)
    city = db.Column(db.String(50))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
