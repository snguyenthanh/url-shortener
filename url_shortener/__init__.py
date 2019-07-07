from os import environ

from gino.ext.sanic import Gino
from sanic import Blueprint, Sanic


app = Sanic(__name__)
app.config.DB_HOST = environ.get("DB_HOST", "localhost")
app.config.DB_USER = environ.get("DB_USER", "postgres")
app.config.DB_PASSWORD = environ.get("DB_PASSWORD")
app.config.DB_DATABASE = environ.get("DB_DATABASE", "postgres")

# Initialize the DB before doing anything else
# to avoid circular importing
db = Gino()
db.init_app(app)


# The blueprints and models will import `db`
from url_shortener.users.views import blueprint as account
from url_shortener.urls.views import blueprint as urls
from url_shortener.views import blueprint as root
from url_shortener.models import Url, User
from url_shortener.exceptions import server_error_handler

blueprints = Blueprint.group(root, account, urls)
app.blueprint(blueprints)
# app.error_handler.add(Exception, server_error_handler)
