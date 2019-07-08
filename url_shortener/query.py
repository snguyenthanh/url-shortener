from time import sleep
from url_shortener import db


async def execute(func):
    """Execute a SQL query in a transaction."""

    # TO-DO: Implement a retry mechanism with exponential backoff
    # if necessary
    async with db.transaction() as tx:
        await func()
