from flask import Flask
from models import db
from routes import app_routes
from config import Config
import socket

app = Flask(__name__)
app.config.from_object(Config)  # Stelle sicher, dass Config geladen wird!

app.register_blueprint(app_routes)

if __name__ == '__main__':# Erstellt die Tabellen, falls nicht vorhanden
    app.run(debug=True)
