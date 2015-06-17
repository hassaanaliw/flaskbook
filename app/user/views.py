from flask import request, flash, url_for, redirect, render_template, abort, g, Blueprint, Response
from app import db, app, login_manager
from app.helpers import get_following_posts, get_self_posts, Messages
from app.user.models import User
from app.posts.models import Posts
from flask.ext.login import login_user, logout_user, current_user, login_required


users = Blueprint('users', __name__)


@users.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """
    The main page of the web app. If POST Request, then create post.
    Else, show the user's feed
    """
    if request.method == "POST":
        '''
        If the request is POST, create a post object and add it to the database
        Assign current_user as the creator of the text post.
        Redirect to the index page
        '''
        post = Posts(request.form['text'])
        post.user = current_user
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))

    user = current_user
    friends_posts = get_following_posts(current_user.id)
    self_posts = get_self_posts(current_user.id)

    return render_template('index.html', user=user, self_posts=self_posts, posts=friends_posts)


@users.route('/follow/<user_id>')
@login_required
def follow(user_id):
    """
    Check if:
        1) The user is logged in.
        2) He is not already following the user and the user exists.
        3) Is not user himself
    If checks pass, update user's followers and following.
    """
    user = current_user
    to_be_followed = User.query.get(user_id)
    if not user or not to_be_followed or user_id == str(current_user.id):
        return Response(status=403)
    if user.following and user_id in user.following:
        return Response(status=403)

    if not user.following:
        user.following = "%s," % user_id
    else:
        user.following += "%s," % user_id

    if not to_be_followed.followers:
        to_be_followed.followers = "%s," % user.id
    else:
        to_be_followed.followers += "%s," % user.id


    db.session.commit()
    return Response(status=200)


@users.route('/unfollow/<user_id>')
@login_required
def unfollow(user_id):
    """
    Check if:
        1) The user is logged in.
        2) He is following the user and the user exists.
        3) Is not user himself
    If checks pass, update user's followers and following.
    """
    user = current_user
    to_be_unfollowed = User.query.get(user_id)
    if not user or not user.following or not to_be_unfollowed or not to_be_unfollowed.followers:
        return Response(status=403)
    if user_id not in user.following or str(user.id) not in to_be_unfollowed.followers:
        return Response(status=403)

    following = user.following.split(",")
    following.remove(str(user_id))
    user.following = ",".join(following)

    followers = to_be_unfollowed.followers.split(",")
    followers.remove(str(user.id))
    to_be_unfollowed.followers = ",".join(followers)

    db.session.commit()
    return Response(status=200)


@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    If the user is already logged in, redirect him to the main page.
    Check if the email is registered and the password hash matches.
    Login and redirect to index.html
    """
    if current_user.is_authenticated():
        return redirect(url_for('.index'))
    if request.method == "GET":
        return render_template('login.html')

    email = request.form['email']
    password = request.form['password']
    remember_me = True
    registered_email = User.query.filter_by(email=email).first()
    if registered_email is None:
        flash(Messages.LOGIN_ERROR_MESSAGE, 'error')
        return redirect(url_for('.login'))
    if not registered_email.check_password(password):
        flash(Messages.LOGIN_ERROR_MESSAGE, 'error')
        return redirect(url_for('.login'))

    login_user(registered_email, remember=remember_me)
    flash(Messages.LOGIN_SUCCESSFUL_MESSAGE)
    return redirect(request.args.get('next') or url_for('.index'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    username = request.form['username']
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']

    if User.query.filter_by(email=email).first():
        flash('E-Mail already in use.')
        return redirect(url_for('.register'))
    if User.query.filter_by(username=username).first():
        flash('Username already in use.')
        return redirect(url_for('.register'))

    user = User(name, request.form['password'], email, username)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.login'))


@app.route('/profile/<username>')
@login_required
def profile(username):
    """
    Check if user exists and if current_user is following. Render profile page.
    """
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)
    if current_user.following and str(user.id) in current_user.following:
        following = True
    else:
        following = False

    posts = Posts.query.filter_by(user_id=user.id).order_by(Posts.pub_date.desc()).all()
    return render_template('profile.html', user=user, following=following, posts=posts)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


