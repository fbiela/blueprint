# blueprint

Frederico Sales <fredericosales@globo.com>
2017

# SQLAlchemy

# sqlite:
sqlite:////absolute/path/to/foo.db

# mysql:
 mysql://scott:tiger@localhost/mydatabase

# postgresql:
postgresql://scott:tiger@localhost/mydatabase

# oracle:
oracle://scott:tiger@127.0.0.1:1521/sidname

# obs:
SQLALCHEMY_TRACK_MODIFICATIONS = True

Integer      ->   db.Integer      ->  an integer
String(size) ->   db.String       ->  a string with max length
Text         ->   db.Text         ->  some longer unicode text
DateTime     ->   db.DateTime     ->  date and time as python datetime object
Float        ->   db.Float        ->  stores float point values
Boolean      ->   db.Boolean      ->  stores a boolean value
PickleType   ->   db.PickleType   ->  stores a pickle python object
LargeBinary  ->   db.LargeBinary  ->  stores large arbitrary binary data
