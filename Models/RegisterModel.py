import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://dbAdmin:Rawman03@cluster0.ljibd.mongodb.net/users?retryWrites=true&w=majority")
        self.db = self.client["users"]
        self.col = self.db["user"]


    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.col.insert_one({"email": data.email, "username": data.username, "password": hashed})
        print("uid is", id.inserted_id)
