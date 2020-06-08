#coding: UTF-8
from flask import Flask
import flask_sqlalchemy

import config

# def create_app(db):
def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

    flask_app.app_context().push()
    # db.init_app(flask_app)
    # db.create_all()

    # seed()

    return flask_app
