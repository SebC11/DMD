import pymongo
import bcrypt
from pymongo import MongoClient


class LoginModel:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://dbAdmin:Rawman03@cluster0.ljibd.mongodb.net/users?retryWrites=true&w=majority")
        self.db = self.client["users"]
        self.col = self.db["user"]

    def check_login(self,data):
        print("in check")
        user = self.col.find_one({"email": data.email})

        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False