import os
from api.app import create_app

api = create_app(os.getenv("FLASK_ENV"))
