#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse
from db import db

from models.song import SongModel

from utils.date_format import getTimeStamp


class SongList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username2",
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def get(self):
        data = self.parser.parse_args()
        username = data["username2"]

        songs = [song.json() for song in SongModel.find_by_username(username)]

        return {
                   "status": 200,
                   "message": "Get success list",
                   "data": [song for song in songs],
                   "total": len(SongModel.find_all())
               }, 200


class SongRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("artists",
                        type=dict,
                        action='append',
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = self.parser.parse_args()

        for artist in data["artists"]:
            username = artist["username"]
            db.session.query(SongModel).filter_by(username=username).delete()
            db.session.commit()

        for artist in data["artists"]:
            username = artist["username"]
            artist_id = artist["artist_id"]
            artist_name = artist["artist_name"]

            if SongModel.find_by_artist_id(artist_id, username):
                pass
            else:
                song = SongModel(username, artist_id, artist_name, getTimeStamp(), None, None, None)
                song.save_to_db()

        return {
                   "status": 200,
                   "message": "Successfully."
               }, 200
