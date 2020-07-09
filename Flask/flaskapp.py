from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8a74d6b55af7824f00b861cf3b445fbe' # A secret key signs cookies when a user visits the site and therefore prevents cookie tampering

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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts= posts, title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Thank you {form.username.data}. Your account has now been created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@boc.com' and form.password.data == 'afeDudm9!':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Account not found. Please check your username and password and try again.', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__== '__main__':
    app.run(debug= True)
    



