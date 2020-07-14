# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# configure our database
DATABASE = {
    'name': 'id.db'
}
SQLALCHEMY_DATABASE_URI = 'sqlite:///id.db'

DEBUG = True
PORT = 5000
SECRET_KEY = 'thisisnotsafe'

def create_app():

    app = Flask(__name__)
    app.config.from_object(__name__)

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    return app
