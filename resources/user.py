import sqlite3

from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister():
    def post(username,password,email):

        #we will use the function already present in user class
        if UserModel.find_by_username(username):
            return 400

        user = UserModel(username,password,email) #this assigns the data respectively
        user.save_to_db()
        return 200
