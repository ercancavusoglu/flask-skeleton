from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import yaml

template_yaml = yaml.load(open('config/template.yaml'), Loader=yaml.FullLoader)
template_folder = template_yaml["parameters"]["folder_path"]

app = Flask(__name__, template_folder=template_folder)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

from app.http import routes
