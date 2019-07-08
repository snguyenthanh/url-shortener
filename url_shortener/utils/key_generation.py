from os import urandom
from base64 import b32encode
from math import log as logarithm
from random import randint
from url_shortener.models import Url


async def generate_random_url_alias(
    _urandom=urandom, _encode=b32encode, _randint=randint, _factor=logarithm(256, 32)
):
    # The length of URL alias is 8-12 characters
    count = _randint(8, 12)

    # count + 1 / _factor gives us the number of bytes needed
    # to produce *at least* count encoded characters
    random_str = (
        _encode(_urandom(int((count + 1) / _factor)))[:count].decode("ascii").lower()
    )

    while await Url.query.where(Url.url_alias == random_str).gino.first():
        random_str = (
            _encode(_urandom(int((count + 1) / _factor)))[:count]
            .decode("ascii")
            .lower()
        )
    return random_str
