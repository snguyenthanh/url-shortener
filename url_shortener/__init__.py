from os import environ

from sanic import Blueprint, Sanic

from aiomysql import create_pool
from url_shortener.accounts.urls import blueprint as account
from url_shortener.urls import blueprint as root

blueprints = Blueprint.group(root, account)

async def setup_db():
    pool = await create_pool(
        host=os.environ.get('DATABASE_URL', '127.0.0.1'),
        port=os.environ.get('DATABASE_PORT', 3306),
        user=environ['DATABASE_USERNAME'],
        password=environ['DATABASE_PASSWORD'],
        db=environ['DATABASE_INSTANCE']
    )
    return pool


def create_application():
    app = Sanic(__name__)
    app.blueprint(blueprints)
	app.db = setup_db()

    return app

__all__ = ['create_application']
