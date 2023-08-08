from flask import Flask

app = Flask(__name__)

from app import routes

# Export the Flask app
from app import app as flask_app