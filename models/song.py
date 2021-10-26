from db import db
from utils.date_format import getTimeStringFromTimeStamp
from sqlalchemy import desc


class SongModel(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, comment="Username")
    artist_id = db.Column(db.String(100), nullable=False, comment="Artist id")
    artist_name = db.Column(db.String(100), nullable=False, comment="Artist name")
    created_at = db.Column(db.Integer, nullable=True, comment="Timestamp")
    created_by = db.Column(db.String(30), nullable=True, comment="Timestamp")
    updated_at = db.Column(db.Integer, nullable=True, comment="Timestamp")
    updated_by = db.Column(db.String(30), nullable=True, comment="Timestamp")

    def __init__(self, username, artist_id, artist_name, created_at, created_by, updated_at, updated_by):
        self.username = username
        self.artist_id = artist_id
        self.artist_name = artist_name
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'artist_id': self.artist_id,
            'artist_name': self.artist_name,
            'created_at': self.created_at,
            'created_at_string': None if self.created_at is None else getTimeStringFromTimeStamp(self.created_at),
            'created_by': self.created_by,
            'updated_at': self.updated_at,
            'updated_at_string': None if self.updated_at is None else getTimeStringFromTimeStamp(self.updated_at),
            'updated_by': self.updated_by
        }

    @classmethod
    def find_by_artist_id(cls, artist_id, username):
        return cls.query.filter_by(artist_id=artist_id, username=username).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.order_by(desc(cls.created_at)).all()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
