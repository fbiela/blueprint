"""Import."""
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, insert, update

from flask_bcrypt import Bcrypt

app = Flask('database')
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    """__tablename__ user."""

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, unique = True)
    name = db.Column(db.Text)
    email = db.Column(db.Text, unique = True)
    password = db.Column(db.Text)
    notifications = db.Column(db.Boolean)

    def __init__(self, username = '', name = '', email = '', password = '', notifications = ''):
        """Constructor."""
        self.username = username
        self.name = name
        self.email = email
        self.password = password
        self.notifications = notifications

    def __repr__(self):
        """Dummy."""
        return '<User %r>' % self.name
