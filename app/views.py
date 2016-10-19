from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Jobling'} # fake user
	posts = [ # fake array of posts
		{
			'author': {'nickname': 'Tiago'},
			'body': 'Está um lindo dia para comer bolos!'
		},
		{
			'author': {'nickname': 'Rita'},
			'body': 'Podemos ir passear!'
		}
	]
	return render_template('index.html',
							title = 'Home',
							user = user,
							posts = posts)
