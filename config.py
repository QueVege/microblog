import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', default='you-will-never-guess')
