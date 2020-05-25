from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm, PostForm
from app.models import User, Post
from flask_login import current_user, login_user, logout_user, login_required
from app.urlParse import FetchItem

# @login_required

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        page = form.post.data
        r = FetchItem()
        body=r.fetch(page)
        if body is not False:
            body=r.fetch(page)['body']
            price=r.fetch(page)['price']
            post = Post(body=body, price=price, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Added item!')
            return redirect('/home')
        else:
            flash('Invalid url!')
    posts = Post.query.filter_by(user_id=int(current_user.get_id()))
    quantity = posts.count()
    return render_template("index.html", title="Home", form=form, posts=posts, quantity=quantity)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect('/home')
    return render_template("login.html", title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/home')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You did it!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route('/delete/<post_id>')
@login_required
def delete(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/home')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500