#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import spotipy
import random

from flask_restful import Resource, reqparse
from lyricsgenius import Genius
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = "2bf8ef3c695b4530b8b3ca5d6ad6e320"
os.environ['SPOTIPY_CLIENT_SECRET'] = "bba39cdff4d7401dbeef3e562f709f3a"
os.environ['GENIUS_ACCESS_TOKEN'] = "YIu1Ei1zTaocoj6LAvEb20Z8dchGdTK3vVHs7c9eNbTrXlREjznGbMdZousdjXUd"


def get_preview(link):
    if link is None:
        return ""
    return link


class ArtistList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("artist_id",
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def get(self):
        data = self.parser.parse_args()

        artist_id = data["artist_id"]
        url = f"spotify:artist:{artist_id}"

        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

        try:
            results = spotify.artist_top_tracks(url, country='US')
            top_tracks_artistname = []
            top_tracks_name = []
            top_tracks_preview = []
            top_tracks_art = []

            for track in results['tracks'][:]:
                ('track    : ' + track['artists'][0]['name'])
                ('track    : ' + track['name'])
                ('audio    : ' + get_preview(track['preview_url']))
                ('cover art: ' + track['album']['images'][0]['url'])

                top_tracks_artistname.append(track['artists'][0]['name'])
                top_tracks_name.append(track['name'])
                top_tracks_preview.append(track['preview_url'])
                top_tracks_art.append(track['album']['images'][0]['url'])

            num = random.randrange(10)

            trackartistname = top_tracks_artistname[num]
            trackname = top_tracks_name[num]

            if track['preview_url']:
                trackpreview = top_tracks_preview[num]
            else:
                trackpreview = ""

            trackart = top_tracks_art[num]

            genius = Genius()
            songlyr = genius.search_song(trackname, trackartistname)

            if songlyr is not None:
                song_lyr = songlyr.url
            else:
                song_lyr = ""

            return {
                       "message": "Success",
                       "status": 200,
                       "data": {
                           "trackArtistName": trackartistname,
                           "trackName": trackname,
                           "trackPreview": trackpreview,
                           "trackArt": trackart,
                           "songLyr": song_lyr
                       }
                   }, 200

        except:
            return {
                       "message": "Invalid artist id",
                       "status": 400,
                       "data": None
                   },
