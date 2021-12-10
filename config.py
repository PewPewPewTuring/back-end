import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
  if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/back_end_development"
  else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
