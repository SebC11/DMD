import gridfs
import pymongo
import datetime
import gridfs


class Posts:

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client["users"]
        self.users = self.db["user"]
        self.posts = self.db["posts"]
        self.fs = gridfs.GridFS(self.client.gridfs)

    def insert_post(self, data):
        inserted = self.posts.insert({"username": data.username, "content": data.content, "stars" : 0, "date": datetime.datetime.now(),
                                      "comments": [{"username": "DFA Slanderer", "content": "I think Big M made a piazza post about it. Check it out!" , "date": datetime.datetime.now()}]})
        return True

    def get_all_posts(self):
        all_posts = self.posts.find()
        new_posts = []
        for post in all_posts:
            post['user'] = self.users.find_one({"username": post['username']})
            new_posts.append(post)
        return new_posts

    def get_user_posts(self, user):
        all_posts = self.posts.find({"username": user}).sort('date', pymongo.ASCENDING)
        new_posts = []
        for post in all_posts:
            post['user'] = self.users.find_one({"username": post['username']})
            new_posts.append(post)
        return new_posts

    def get_user(self, username):
        self.users.find_one({"username": username})

    def add_star(self, content, username, stars):
        self.posts.find_one_and_update(
            {"content" : content, "username" : username},
            {"$set":
                {"stars": stars}
            },upsert=True
        )

    def add_comment(self, content, username, pfp_id):
        post = self.posts.find_one({"content" : content, "username" : username})
        post["comments"] = post["comments"] + {"content" : content, "username" : username, "pfp": pfp_id}

    def insert_image(self, image, id):
        image_id = self.fs.put(image, filename=id);
        self.posts.find_one_and_update(
            {"id" : id},
            {"$set":
                 {"image": image_id}
             }, upsert=True
        )
