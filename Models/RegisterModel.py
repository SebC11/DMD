import pymongo
from pymongo import MongoClient


class RegisterModel:

    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://dbAdmin:FAKEUSER@cluster0.ljibd.mongodb.net/FAKETABLENAME?retryWrites=true&w=majority")
        self.db = self.client.users


    def insert_email(self, data):
        print("data is", data);