"""Import."""
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, SelectField,
                     SelectMultipleField, SubmitField, TextAreaField,
                     TextField)
from wtforms.validate import Email, InputRequired, Lenght

app = Flask('forms')
app.config.from_pyfile('app.cfg')
