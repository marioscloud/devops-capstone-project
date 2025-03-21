from flask import Flask
from flask_talisman import Talisman
from service.models import init_db
from flask_cors import CORS

app = Flask(__name__)
Talisman(app)
CORS(app)

# Initialize the database
init_db(app)

# Import the routes after the app and talisman are set up
import service.routes
