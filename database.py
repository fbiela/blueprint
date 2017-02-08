"""Import."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('database')
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)
