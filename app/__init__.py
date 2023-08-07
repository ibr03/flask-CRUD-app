from flask import Flask
from pymongo import MongoClient
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

client = MongoClient(app.config['MONGO_URI'])
db = client.get_default_database()

# Print a message confirming the MongoDB connection
print("Connected to MongoDB!")

from .routes import *