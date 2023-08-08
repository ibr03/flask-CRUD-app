from .. import db
from bson.objectid import ObjectId

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        db.users.insert_one({
            'name': self.name,
            'email': self.email,
            'password': self.password
        })

    @staticmethod
    def get_all():
        return list(db.users.find({}, {'_id': False}))

    @staticmethod
    def get_by_id(user_id):
        return db.users.find_one({'_id': ObjectId(user_id)}, {'_id': False})

    def update(self, user_id):
        db.users.update_one({'_id': ObjectId(user_id)}, {'$set': {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }})

    @staticmethod
    def delete(user_id):
        db.users.delete_one({'_id': ObjectId(user_id)})
