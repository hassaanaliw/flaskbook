from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from app import db

class User(db.Model):
    """
    This is the main User Table for our database. It contains all the user's information including
    the User's name, email, password, followers, those who he is following and Posts.
    """
    __tablename__ = "users"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(40), index=True)
    name = db.Column('name', db.String(40), index=True, unique=True)
    password = db.Column('password', db.String(250))
    email = db.Column('email', db.String(50), unique=True, index=True)
    registered_on = db.Column('registered_on', db.DateTime)
    posts = db.relationship('Posts', backref='user', lazy='dynamic')
    following = db.Column('following', db.String)
    followers = db.Column('followers', db.String)

    def __init__(self, name, password, email, username):
        self.name = name
        self.username = username.lower()
        self.set_password(password)
        self.email = email   
        self.registered_on = datetime.utcnow()


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


    def __repr__(self):
        return '<User %r>' % self.username


