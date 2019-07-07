from sanic import Blueprint, response
from url_shortener.models import Url


blueprint = Blueprint("root")


@blueprint.route("/<url_hash>")
async def redirect_url_from_hash(request, url_hash):
    # TO-DO: serve the GET request from cache
    url = await Url.query.where(Url.url_hash == url_hash).gino.first()
    if not url:
        return response.text("404 - Page Not Found")

    return response.redirect("http://" + url.actual_url)
