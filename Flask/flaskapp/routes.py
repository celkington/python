from flask import render_template, url_for, flash, redirect, request
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
     'author': 'Chris',
     'title': 'Blog Post 1',
     'content': 'This is some text',
     'post_date': '6/20/2020'
     },
        {
     'author': 'John',
     'title': 'Blog Post 2',
     'content': 'This is some other text',
     'post_date': '6/21/2020'
     }
    ]


# Webpages within the website
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts= posts, title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Thank you {form.username.data}. Your account has now been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'You have successfully logged in as {form.email.data}', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Either email or password not found. Please check your email and password and try again.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')