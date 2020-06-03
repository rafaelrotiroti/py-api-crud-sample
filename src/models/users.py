from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def configuration(app):
    db.init_app(app)
    app.db = db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, name, username,password):
        self.name = name
        self.username = username
        self.password = password

