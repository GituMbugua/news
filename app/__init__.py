from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
# from config import config_options

# def create_app(config_name):
app = Flask(__name__, instance_relative_config = True)

# initialize flask extensions
bootstrap = Bootstrap(app)

# set up config
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views