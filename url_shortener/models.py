from time import time
from url_shortener import db


def unix_time():
    """Return an unix timestamp."""
    return int(time())


class Url(db.Model):
    __tablename__ = "urls"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    url_alias = db.Column(db.String)
    actual_url = db.Column(db.String)
    created_at = db.Column(db.BigInteger, default=unix_time)
    updated_at = db.Column(db.BigInteger, onupdate=unix_time)
    owner_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))

    # Index
    _idx_url_alias = db.Index("idx_url_alias", "url_alias", unique=True)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    password = db.Column(db.String)  # TO-DO: Add arg `null=False`
    created_at = db.Column(db.BigInteger, default=unix_time)
    api_key = db.Column(db.String)

    # Index
    _idx_username = db.Index("idx_username", "username", unique=True)
    _idx_api_key = db.Index("idx_api_key", "api_key", unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._urls = set()

    def __repr__(self):
        return "{}:{}".format(self.username, self.id)
