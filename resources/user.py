#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decouple import config
from flask_restful import Resource, reqparse

from models.user import UserModel

from utils.date_format import getTimeStamp

UPLOAD_IMAGE_PATH = config("UPLOAD_IMAGE_PATH")


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = self.parser.parse_args()

        username = data["username"]
        if UserModel.find_by_username(username):
            return {
                       "message": "Account '{}' already exists".format(username)
                   }, 400
        else:
            user = UserModel(username, getTimeStamp(), None, None, None)
            user.save_to_db()

            return {
                       "message": "Account '{}' successfully created.".format(username)
                   }, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = self.parser.parse_args()
        user = UserModel.find_by_username(data["username"])
        if user:
            return {
                       "message": "Logged in successfully"
                   }, 200
        else:
            return {
                       "message": "Login failed"
                   }, 401
