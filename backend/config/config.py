import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://usuario:contraseña@localhost/taller')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
