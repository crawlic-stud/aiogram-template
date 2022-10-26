import pymongo


class Database:
    def __init__(self, url, db_name, collection_name):
        self.client = pymongo.MongoClient(url)[db_name][collection_name]

    def get_by_name(self, name):
        return self.client.find_one({"name": name})

    def get_all(self):
        return [r for r in self.client.find()]
