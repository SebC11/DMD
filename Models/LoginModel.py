import pymongo
import bcrypt
from pymongo import MongoClient


class LoginModel:

    def __init__(self):
        self.client = pymongo.MongoClient("DUMMY")
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