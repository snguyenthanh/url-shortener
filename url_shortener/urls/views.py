from sanic import Blueprint, response
from sanic.exceptions import InvalidUsage

from url_shortener.models import Url
from url_shortener.validation import validate_request_data
from url_shortener.query import execute
from url_shortener.exceptions import UniqueViolationError
from url_shortener.serializers import UrlSerializer
from url_shortener.utils.key_generation import generate_random_url_alias
from url_shortener.utils.urls import get_url

blueprint = Blueprint("urls", url_prefix="/server/urls")


@validate_request_data(schema="UrlCreate")
async def create_url(request):
    req_data = request.json
    url_alias = req_data.get("url_alias")

    # Check if an URL exists before creating it
    if url_alias and await Url.query.where(Url.url_alias == url_alias).gino.first():
        raise UniqueViolationError("url_alias", req_data["url_alias"])

    # Generate a random key if not provided
    if not url_alias:
        url_alias = await generate_random_url_alias()

    # Overwrite 'url_alias' in request.json
    url_obj = Url(**dict(req_data, url_alias=url_alias))
    await execute(url_obj.create)
    url_data = UrlSerializer(url_obj).data
    return response.json({"data": url_data})


@validate_request_data(schema="UrlUpdate")
async def update_url(request):
    url_obj = await get_url(request)

    # Validate the key-values to be updated
    req_data = request.json
    _hasattr = hasattr
    for key in req_data.keys():
        if not _hasattr(url_obj, key):
            raise InvalidUsage("URL instance doesn't have attribute '{}'".format(key))

    # Update the values of `url_obj` from request's body
    await url_obj.update(**req_data).apply()

    url_data = UrlSerializer(url_obj).data
    return response.json({"data": url_data})

@validate_request_data(allow_empty=True)
async def delete_url(request):
    url_obj = await get_url(request)

    await url_obj.delete()
    return response.text("")


@blueprint.route("/", methods=["POST", "PUT", "DELETE"])
async def create_update_delete_url(request):
    func_mapping = {"POST": create_url, "PUT": update_url, "DELETE": delete_url}
    result = await func_mapping[request.method](request)
    return result
