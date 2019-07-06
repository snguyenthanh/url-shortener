from url_shortener import db


class Url(db.Model):
    __tablename__ = "urls"
    id = db.Column(db.BigInteger, primary_key=True)
    shortened_url = db.Column(db.String)
    full_url = db.Column(db.String)
    owner_id = db.Column(db.BigInteger, db.ForeignKey("users.id"))

    # Index
    _idx_shortened_url = db.Index("idx_shortened_url", "shortened_url", unique=True)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String)

    # Index
    _idx_username = db.Index("idx_username", "username", unique=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._urls = set()

    def __repr__(self):
        return "{}:{}".format(self.username, self.id)

    @property
    def urls(self):
        return self._urls

    @urls.setter
    def add_url(self, url):
        self._urls.add(url)
