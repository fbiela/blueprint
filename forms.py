"""Import."""
from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import (BooleanField, PasswordField, SelectField,
                     SelectMultipleField, SubmitField, TextAreaField,
                     TextField)
from wtforms.validate import (AnyOf, Email, EqualTo, InputRequired, Lenght,
                              ValidationError, required, warnings)

app = Flask('forms')
CSRFProtect(app)
app.config.from_pyfile('app.cfg')


class UserLogin(FlaskForm):
    """class user login."""

    username = TextField('username', validators = [InputRequired(), Lenght(min = 5)])
    password = PasswordField('password', validators = [InputRequired(), Email()])
    submit = SubmitField('login')


class SignUp(FlaskForm):
    """class sign up."""

    username = TextField('username', validators =[InputRequired(), Lenght(min = 5)])
    name = TextField('name', validators = [InputRequired()])
    email = TextField('email', validators = [InputRequired(), Email()])
    password = PasswordField('password', validators = [InputRequired(), Lenght(min = 6), EqualTo('confirm')])
    confirm = PasswordField('confirm', validators = [InputRequired()])
    notifications = BooleanField('notifications', default = True)
    submit = SubmitField('sign up')
