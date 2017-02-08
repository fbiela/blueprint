# blueprint

[Frederico Sales](mailto:fredericosales@globo.com) - 2017

> flask work box

## requirements docs

- [Flask](http://flask.pocoo.org/docs/0.12/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-Admin](https://flask-admin.readthedocs.io/en/latest/)
- [Flask-Mail](https://pythonhosted.org/Flask-Mail/)
- [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
- [Flask-Classy](https://pythonhosted.org/Flask-Classy/)
- [Flask-Dashed](https://github.com/jeanphix/Flask-Dashed/tree/master/docs)
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask-Openid](https://pythonhosted.org/Flask-OpenID/)
- [Flask-Security](https://pythonhosted.org/Flask-Security/)
- [Flask-Uploads](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/)
- [Flask-Themes](https://pythonhosted.org/Flask-Themes/)
- [Flask-User](https://pythonhosted.org/Flask-User/)
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
- [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/)
- [Numpy](https://docs.scipy.org/doc/numpy/reference/)
- [Reportlab](http://www.reportlab.com/documentation/)
- [Matplotlib](http://matplotlib.org/contents.html)
- [Pysqlite](https://pysqlite.readthedocs.io/en/latest/index.html)
- [Psycopg2](http://initd.org/psycopg/docs/)

## Mail

- MAIL_SERVER = 'smtp.server.net'
- MAIL_PORT = 25
- MAIL_USE_SSL = False
- MAIL_USE_TTL = False
- MAIL_USERNAME = 'username@server.com'
- MAIL_PASSWORD = 'secret_password'

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
