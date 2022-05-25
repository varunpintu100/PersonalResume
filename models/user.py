import sqlite3

from database import db


class UserModel(db.Model):
    __tablename__='users'

    #We are creating the coloumns for the table in the database

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))
    email=db.Column(db.String(80))

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email=email

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first() #this code is used to filter the search and get the first one

    @classmethod
    def find_by_id(cls,user_id):
        return cls.query.filter_by(id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()
