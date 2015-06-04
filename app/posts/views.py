__author__ = 'hassaanaliw'

from flask import Blueprint, Response, redirect, url_for
from app import db
from app.posts.models import Posts
from flask.ext.login import current_user, login_required


posts = Blueprint('posts', __name__)


@posts.route('/like/<post_id>')
@login_required
def like(post_id):
    post = Posts.query.get(post_id)
    if str(current_user.id) in post.liked_by:
        return Response(status=201)
    post.liked_by += str(current_user.id) + ","
    post.likes += 1
    db.session.commit()
    return Response(status=200)


@posts.route('/unlike/<post_id>')
@login_required
def unlike(post_id):
    post = Posts.query.get(post_id)
    if str(current_user.id) not in post.liked_by:
        return Response(status=200)

    liked_by = post.liked_by.split(",")
    liked_by.remove(str(current_user.id))
    post.liked_by = ','.join(liked_by)
    post.likes -= 1
    db.session.commit()
    return Response(status=200)


@posts.route('/delete/<post_id>')
@login_required
def delete(post_id):
    post = Posts.query.get(post_id)
    if not post or post.user_id != current_user.id:
        return redirect(url_for('users.index'))

    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('users.index'))