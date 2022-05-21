import sqlite3

from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister():
    def post(username,password):

        #we will use the function already present in user class
        if UserModel.find_by_username(username):
            return 400

        user = UserModel(username,password) #this assigns the data respectively
        user.save_to_db()
        return 200
