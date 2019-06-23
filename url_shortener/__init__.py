from sanic import Blueprint, Sanic

from url_shortener.accounts.urls import blueprint as account
from url_shortener.urls import blueprint as root

blueprints = Blueprint.group(root, account)

def create_application():
    app = Sanic(__name__)
    app.blueprint(blueprints)
    for handler, (rule, router) in app.router.routes_names.items():
        print('URL: ', rule)
    print()
    
    return app

__all__ = ['create_application']
