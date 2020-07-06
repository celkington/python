from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('home.html', posts= posts, title = 'Home..')

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

