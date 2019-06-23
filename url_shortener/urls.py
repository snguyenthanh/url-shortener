from sanic import Blueprint, response

blueprint = Blueprint('root')

@blueprint.route('/<url_id>')
async def redirect_url_from_id(request, url_id):
    return response.redirect('https://www.google.com')
