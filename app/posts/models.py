from datetime import datetime
from app import db

__author__ = 'hassaanali'

class Posts(db.Model):

    __tablename__ = 'Posts'
    id = db.Column('post_id', db.Integer, primary_key=True)
    text = db.Column('text', db.String)
    pub_date = db.Column('pub_date', db.DateTime)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
    likes = db.Column('likes', db.Integer, default=0)
    liked_by = db.Column('liked_by', db.String, nullable=False)

    def __init__(self, text):
        self.text = text.strip()
        self.liked_by = ""
        self.pub_date = datetime.utcnow()

