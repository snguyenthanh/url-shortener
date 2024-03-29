from functools import partial
from cerberus import Validator
from sanic import response
from sanic.exceptions import InvalidUsage

from url_shortener.exceptions import SchemaValidationError

# Validation Schemas

UrlCreateSchema = {
    "id": {"readonly": True},
    "url_alias": {"type": "string"},
    "actual_url": {"type": "string", "required": True},
    "created_at": {"readonly": True},
    "updated_at": {"readonly": True},
    "owner_id": {"type": "integer", "required": True},
}

UrlUpdateSchema = {
    "id": {"readonly": True},
    "url_alias": {"type": "string"},
    "actual_url": {"type": "string"},
    "created_at": {"readonly": True},
    "updated_at": {"readonly": True},
    "owner_id": {"type": "integer"},
}

UserSchema = {
    "id": {"readonly": True},
    "username": {"type": "string", "required": True},
    "created_at": {"readonly": True},
    "api_key": {"readonly": True},
}


# Decorator for validation

model_mapping = {
    "User": UserSchema,
    "UrlCreate": UrlCreateSchema,
    "UrlUpdate": UrlUpdateSchema,
}


def validate_request_data(func=None, schema=None, allow_empty=False):
    """
    Validate the request data to ensure private fields are protected.

    Raise:
        sanic.exceptions.InvalidUsage: Failed when parsing body as json
            If `request.json` fails to execute.
    """
    if func is None:
        return partial(validate_request_data, schema=schema, allow_empty=allow_empty)

    def inner(request, *args, **kwargs):
        req_data = request.json
        if not allow_empty and not req_data:
            raise InvalidUsage("The request's body must not be empty.")

        if schema and schema in model_mapping:
            validator = Validator()
            _schema = model_mapping[schema]
            if not validator.validate(req_data, _schema):
                raise SchemaValidationError(validator.errors)
        return func(request, *args, **kwargs)

    return inner
