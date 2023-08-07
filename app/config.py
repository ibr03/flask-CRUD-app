import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PORT = os.environ.get('PORT')
    MONGO_URI = os.environ.get('MONGO_URI')