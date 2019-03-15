from flask import render_template, request, redirect, url_for, abort
from . import main
from ..models import User, Post
from .forms import PostForm
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
# from ..email import mail_message


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to app of blog'

    blogs = Post.get_blogs()
    return render_template('index.html',title = title, blogs = blogs)


@main.route('/user/<username>')
@login_required
def user(username):
    """View function that returns the homepage for a particular user when they sign in"""
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user.html', user=user, posts=posts)


@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('posts.html', posts=[post])

@main.route('/blog/new',methods=['GET','POST'])
@login_required
def new_blog():
    form = PostForm()
    if form.validate_on_submit():
        Blog_post = form.content.data
        new_blog = Post(body=Blog_post)
        new_blog.save_post()
        return redirect(url_for('main.index'))
    return render_template('blogs.html', form = form)

@main.route('/blog/new/view')
def view_blog():
    blog = Post.query.filter_by()
    blogs = Post.query.filter_by()
    return render_template('index.html',blog=blog,blogs=blogs)


@main.route('/blog/new/comment/<int:id>',methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comments(comment_name = form.comment_name.data,user=current_user, blog_id =id)
        new_comment.save_comment()
        return redirect(url_for('.index'))
    return render_template('new_comment.html',form = form)

@main.route('/blog/new/comment/<int:id>/view')
def view_comments(id):
    comment = Comments.query.filter_by(blog_id = id)
    return render_template('comment.html',comment = comment)

@main.route('/delete_comment/<int:id>')
@login_required
def delete_comment(id):
    if current_user.is_authenticated:
        comment = Comments.query.filter_by(id = id).first()
        # comment.delete_comment()
        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('comment.html')



#routing for subscribers
@main.route('/subscribe', methods=['GET','POST'])
def subscriber():
    subscriber_form=SubscriberForm()
    if subscriber_form.validate_on_submit():
        subscriber= Subscriber(email=subscriber_form.email.data,title = subscriber_form.title.data)
        db.session.add(subscriber)
        db.session.commit()
        mail_message("Hey Welcome To My Blog ","email/welcome_subscriber",subscriber.email,subscriber=subscriber)
        subscriber = Blog.query.all()
        blog = Blog.query.all()
    return render_template('subscribe.html',subscriber=subscriber,subscriber_form=subscriber_form,blog=blog)