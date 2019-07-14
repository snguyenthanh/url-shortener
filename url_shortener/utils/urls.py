from sanic.exceptions import InvalidUsage

from url_shortener.models import Url


async def get_url(request):
    """
    Validate the url_id in request's body and return the URL instance from database.

    Args:
        request (sanic.request.Request):
            the request received from `views`.

    Returns:
        url_shortener.models.Url
    """
    url_id = request.raw_args.get("id")

    # Right now, only get the URL by its ID in database.
    # `url_alias` can also be used to query
    if not url_id.isdigit():
        raise InvalidUsage(
            "Parameter 'id' in the query is expected to be an integer, but got '{}'".format(
                url_id
            )
        )
    if not url_id:
        raise InvalidUsage("Missing parameter 'id' as the ID of the URL")

    # Check if an URL exists before updating it
    url_obj = await Url.query.where(Url.id == int(url_id)).gino.first()
    if not url_obj:
        raise InvalidUsage("URL with id '{}' doesn't exist.".format(url_id))

    return url_obj
