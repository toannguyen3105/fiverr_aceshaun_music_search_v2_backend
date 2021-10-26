#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from db import db

from resources.user import UserLogin, UserRegister
from resources.song import SongRegister, SongList
from resources.artist import ArtistList

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)


@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()


api.add_resource(UserLogin, '/login')
api.add_resource(UserRegister, '/register')
api.add_resource(SongRegister, '/songs')
api.add_resource(SongList, '/songs-list')
api.add_resource(ArtistList, '/artist')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, use_reloader=True, debug=True)
