import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'BliBlaBlub!'
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqlconnector://root:@localhost/webseite')##localhost DB wird aber nicht genutzt
    SQLALCHEMY_TRACK_MODIFICATIONS = False