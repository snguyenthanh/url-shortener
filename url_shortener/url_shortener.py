from sanic import response

from url_shortener.urls import blueprint


@blueprint.route('/<url_id>')
async def redirect_url_from_id(request, url_id):
    return response.redirect('https://www.google.com')
