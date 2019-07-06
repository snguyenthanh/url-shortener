from os import environ

from gino.ext.sanic import Gino
from sanic import Blueprint, Sanic

from url_shortener.users.urls import blueprint as account
from url_shortener.urls import blueprint as root

# Globals
blueprints = Blueprint.group(root, account)
db = Gino()

from url_shortener.models import Url, User

app = Sanic(__name__)
app.config.DB_HOST = environ.get("DB_HOST", "localhost")
app.config.DB_USER = environ.get("DB_USER", "postgres")
app.config.DB_PASSWORD = environ.get("DB_PASSWORD")
app.config.DB_DATABASE = environ.get("DB_DATABASE", "postgres")

app.blueprint(blueprints)
db.init_app(app)
