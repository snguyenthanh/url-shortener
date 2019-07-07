from sanic import Blueprint, response
from url_shortener.models import Url
from url_shortener.validation import validate_request_data
from url_shortener.query import execute
from url_shortener.exceptions import UniqueViolationError

blueprint = Blueprint('urls', url_prefix='/server/urls')

@validate_request_data(schema='UrlCreate')
async def create_url(request):
    """
    Raise:
        asyncpg.exceptions.UniqueViolationError:
            duplicate key value violates unique constraint "urls_pkey"
        DETAIL:  Key (id)=(1) already exists.
    """

    # TO-DO: Auto-generate a `url_hash` if it is not provided
    req_data = request.json
    if await Url.query.where(Url.url_hash == req_data['url_hash']).gino.first():
        raise UniqueViolationError('url_hash', req_data['url_hash'])

    url = Url(**req_data)
    await execute(url.create)
    return response.text('')

@validate_request_data(schema='UrlUpdate')
async def update_url(request):
    return response.text('yay')

@blueprint.route("/", methods=['POST', 'PUT'])
async def create_update_delete_url(request):
    func_mapping = {
        'POST': create_url,
        'PUT': update_url,
    }
    result = await func_mapping[request.method](request)
    return result
