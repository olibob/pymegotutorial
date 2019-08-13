from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'Miguel'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'John'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)