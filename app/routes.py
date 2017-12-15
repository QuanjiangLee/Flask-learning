from app import app
from flask import render_template

@app.route('/index')
def index():
    user = {'userName': 'Quanjiang'}
    title = 'Quanjiang'
    posts = [
    {
        'author': {'userName': 'jokey'},
        'message': 'today is tuesday!'
    },
    {
        'author': {'userName': 'Quanjiang'},
        'message': 'this is a lovely day!'
    }
    ]
    return render_template('posts.html', user=user, title=title, posts=posts)
    #return render_template('index.html', user=user, title=title, posts=posts)

'''
def index():
	user = {'userName': 'Quanjiang'}
	return 
	<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello,  + user['userName'] + !</h1>
    </body>
</html>
'''
