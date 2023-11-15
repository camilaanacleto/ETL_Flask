import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///etl_database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


