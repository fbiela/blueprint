# blueprint

Frederico Sales [fredericosales@globo.com](mailto:fredericosales@globo.com) 2017

## Mail

- MAIL_SERVER = 'smtp.server.net'
- MAIL_PORT = 25
- MAIL_USE_SSL = False
- MAIL_USE_TTL = False
- MAIL_USERNAME = 'username@server.com'
- MAIL_PASSWORD = 'secret_password'

## SQLAlchemy

- flask-sqlalchemy docs

## sqlite:

- sqlite:////absolute/path/to/foo.db

## mysql:

- mysql://scott:tiger@localhost/mydatabase

## postgresql:

- postgresql://scott:tiger@localhost/mydatabase

## oracle:

- oracle://scott:tiger@127.0.0.1:1521/sidname

## obs:

- SQLALCHEMY_TRACK_MODIFICATIONS = True

## Types

type         | object         | description
------------ | -------------- | ---------------------------------------
Integer      | db.Integer     | an integer
String(size) | db.String      | a string with max length
Text         | db.Text        | some longer unicode text
DateTime     | db.DateTime    | date and time as python datetime object
Float        | db.Float       | stores float point values
Boolean      | db.Boolean     | stores a boolean value
PickleType   | db.PickleType  | stores a pickle python object
LargeBinary  | db.LargeBinary | stores large arbitrary binary data
