# config.py

import os
import secrets

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('MY_FLASK_SECRET_KEY', secrets.token_hex(16))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Ścieżka do pliku bazy danych SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Zalecane dla Flask SQLAlchemy

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    # Inne ustawienia dla środowiska deweloperskiego
