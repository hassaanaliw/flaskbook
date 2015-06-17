__author__ = 'hassaanaliw'

'''
Includes several helper functions for the main app that are used a number of
times to avoid using code multiple times.
'''

from app.posts.models import Posts
from app.user.models import User


class Messages():
    LOGIN_ERROR_MESSAGE = "Email/Password is Wrong. Please Try Again."
    LOGIN_SUCCESSFUL_MESSAGE = "Logged in Successfully."
    REGISTER_EMAIL_EMPTY_MESSAGE = "The Email Field Cannot be Empty."
    REGISTER_PASSWORD_EMPTY_MESSAGE = "The Password Field Cannot be Empty."
    REGISTER_EMAIL_EXISTS_MESSAGE = "An Account is already registered with this Email."
    REGISTER_USERNAME_EXISTS_MESSAGE = "An Account is already registered with this Username."


def get_self_posts(user_id):
    """
    Returns Posts submitted by current user.
    """
    posts = Posts.query.filter_by(user_id=user_id).order_by(Posts.pub_date.desc()).all()
    return posts


def get_following_posts(user_id):
    """
    Returns Posts submitted by people the user follows.
    """
    user = User.query.get(user_id)
    if not user or not user.following:
        return []

    friends = user.following.split(',')
    # Postgres doesn't play well with empty elements. Raises sqlalchemy.exc.DataError exception
    friends.remove(u'')
    posts = Posts.query.filter(Posts.user_id.in_(friends)).order_by(Posts.pub_date.desc()).all()

    return posts


