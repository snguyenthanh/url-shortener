from sanic import Blueprint, response
from url_shortener.models import User

blueprint = Blueprint('users', url_prefix='/server/users')

async def create_user(request):
    return response.text('')

async def update_user(request):
    req_data = request.json
    return response.text('yay')

@blueprint.route("/", methods=['POST', 'PUT'])
async def create_update_delete_user(request):
    func_mapping = {
        'POST': create_user,
        'PUT': update_user,
    }

    result = await func_mapping[request.method](request)
    return result
