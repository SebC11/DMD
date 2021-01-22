import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:

    def __init__(self):
        self.client = pymongo.MongoClient("")
        self.db = self.client["users"]
        self.col = self.db["user"]

    def insert_user(self, data):
        if self.col.find_one({"email":data.email}) is not None:
            return "failure"
        else:
            hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt());
            id = self.col.insert_one({"email": data.email, "username": data.username, "password": hashed, "about" : "N/A",
                                      "birthday" : "N/A", "hobbies" : "N/A", "grade" : "N/A", "least-favorite-course" : "N/A",
                                      "math-courses" : "N/A","name" : "N/A", "university" : "N/A"})
            print("uid is", id.inserted_id)
