from url_shortener import db
from time import time


def unix_time():
    """Return an unix timestamp."""
    return int(time())


class Url(db.Model):
    __tablename__ = "urls"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    url_hash = db.Column(db.String)
    actual_url = db.Column(db.String)
    created_at = db.Column(db.BigInteger, default=unix_time)
    updated_at = db.Column(db.BigInteger, onupdate=unix_time)
    owner_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))

    # Index
    _idx_url_hash = db.Index("idx_url_hash", "url_hash", unique=True)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    created_at = db.Column(db.BigInteger, default=unix_time)

    # Index
    _idx_username = db.Index("idx_username", "username", unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._urls = set()

    def __repr__(self):
        return "{}:{}".format(self.username, self.id)
