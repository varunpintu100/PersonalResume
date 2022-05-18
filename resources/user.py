import sqlite3

from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    #this parser will parse through json of the request and make sure that the field is present
    parser.add_argument('username',type=str,required=True,help="This field cannot be blank")

    #this parser will parse through json of the request and make sure that the field is present
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank")

    def post(self):

        #this is used to get the parsed arguments to one place
        data = UserRegister.parser.parse_args()

        #we will use the function already present in user class
        if UserModel.find_by_username(data['username']):
            return {"message":"A user with the uesrname already exists."},400

        user = UserModel(**data) #this assigns the data respectively
        user.save_to_db()
        return {"message":"User created sucessfully."},200
