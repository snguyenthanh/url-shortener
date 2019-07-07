"""
A collection of custom exceptions to return to client.
"""
from sanic.response import json
from sanic.exceptions import SanicException


async def server_error_handler(request, exception):
    status_code = 500
    exc_message = exception

    if hasattr(exception, "args") and exception.args:
        exc_message = exception.args[0]
    if hasattr(exception, "status_code"):
        status_code = exception.status_code

    return json({"error": exc_message}, status=status_code)


class SchemaValidationError(SanicException):
    def __init__(self, message, status_code=422):
        super().__init__(message, status_code)


class UniqueViolationError(SanicException):
    """
    An overwritten error for asyncpg.exceptions.UniqueViolationError.

    Note:
        asyncpg.exceptions.UniqueViolationError:
            duplicate key value violates unique constraint "urls_pkey"
        DETAIL:  Key (id)=(1) already exists.
    """

    def __init__(self, key, value, status_code=422):
        message = (
            "The '{}' with value '{}' already exists. "
            "Please choose a different value for '{}'"
        ).format(key, value, key)
        super().__init__(message, status_code)
