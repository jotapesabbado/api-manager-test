from init import create_app
from flask_restless import APIManager
import flask_sqlalchemy
import datetime
# from structure.models.Computer import Computer
# from structure.models.Person import Person 

# db = flask_sqlalchemy.SQLAlchemy()
app = create_app()
db = flask_sqlalchemy.SQLAlchemy(app=app)

# create_app(db)

# {
# 	"time_end": "2020-06-01T15:31:51",
#     "time_start": "2020-06-01T15:31:52",
#     "total_question": 4,
#     "error_question": 2,
#     "video_replay": 1,
#     "user_id": 1
# }


# Create the Flask-SQLAlchemy models.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(100),  unique=True)
    attempt = db.relationship('Attempt',
                                backref=db.backref('user'))

class Attempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_start = db.Column(db.DateTime(), default=datetime.datetime.utcnow, nullable=False)
    time_end = db.Column(db.DateTime(), default=datetime.datetime.utcnow ,nullable=False)
    total_question = db.Column(db.Integer)
    error_question = db.Column(db.Integer)
    video_replay = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anwser = db.Column(db.Integer)
    choise_1 = db.Column(db.String(100))
    choise_2 = db.Column(db.String(100))
    choise_3 = db.Column(db.String(100))
    choise_4 = db.Column(db.String(100))

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest = db.Column(db.String(100))


# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode(100),  unique=True)
#     birth_date = db.Column(db.Date)
#     computers = db.relationship('Computer',
#                                 backref=db.backref('owner'))

# class Computer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Unicode(100), unique=True)
#     vendor = db.Column(db.Unicode(100))
#     owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
#     purchase_time = db.Column(db.DateTime)


# Create the database tables.
db.create_all()

manager = APIManager(flask_sqlalchemy_db=db)
manager.init_app(app)

manager.create_api(User, app=app, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
manager.create_api(Attempt, app=app, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
manager.create_api(Quiz, app=app, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
manager.create_api(Question, app=app, methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])

if __name__ == "__main__":
    app.run(debug=True)