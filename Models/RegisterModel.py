import pymongo
import gridfs
import bcrypt


class RegisterModel:

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client["users"]
        self.col = self.db["user"]
        self.fs = gridfs.GridFS(self.client.gridfs)

    def insert_user(self, data):
        if self.col.find_one({"email":data.email}) is not None:
            return "failure"
        else:
            hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt());
            # Returns ID where it's stored. Store this value and then do lookup with said value
            b = self.fs.put("static/images/default.png", filename=data.username)
            id = self.col.insert_one({"email": data.email, "username": data.username, "password": hashed, "about" : "N/A",
                                      "birthday" : "N/A", "hobbies" : "N/A", "grade" : "N/A", "least-favorite-course" : "N/A",
                                      "math-courses" : "N/A","name" : "N/A", "university" : "N/A", "pfp" : b})

