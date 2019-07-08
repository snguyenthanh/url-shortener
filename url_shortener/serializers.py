"""
Serializers allow model instances to be converted to Dictionary
that can then be easily rendered into JSON.
"""


class Serializer:
    """
    Followed the structure of Django REST framework's serializer,
    only allow a certain number of fields to be returned to clients.

    This is to ensure no private fields got leaked out.
    """

    fields = ()
    data = {}

    def __init__(self, model):
        _hasattr = hasattr
        _data = {}
        for field in self.fields:
            if _hasattr(model, field):
                _data[field] = getattr(model, field)
        self.data = _data


class UrlSerializer(Serializer):
    fields = ("id", "url_alias", "actual_url", "created_at", "updated_at", "owner_id")


class UserSerializer(Serializer):
    fields = ("id", "username", "created_at")
