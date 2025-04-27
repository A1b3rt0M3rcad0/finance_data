from flask import Flask
from src.main.endpoints import endpoints

app = Flask(__name__)
app.register_blueprint(endpoints)