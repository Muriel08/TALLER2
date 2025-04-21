from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from config.config import Config
from models import db
from routes import register_blueprints

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
CORS(app)
register_blueprints(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
