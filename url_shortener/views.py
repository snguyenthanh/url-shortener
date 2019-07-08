from sanic import Blueprint, response
from url_shortener.models import Url


blueprint = Blueprint("root")


@blueprint.route("/<url_alias>")
async def redirect_url_from_hash(request, url_alias):
    # TO-DO: serve the GET request from cache
    url = await Url.query.where(Url.url_alias == url_alias).gino.first()
    if not url:
        return response.text("404 - Page Not Found")

    return response.redirect("http://" + url.actual_url)
