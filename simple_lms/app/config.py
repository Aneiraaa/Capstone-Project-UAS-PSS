import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:root@localhost:3306/simple_lms')
    SQLALCHEMY_TRACK_MODIFICATIONS = False