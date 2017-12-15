from flask import render_template, flash, redirect
from app import app
from .forms import loginForm

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = loginForm()
	if form.validate_on_submit():
		flash('login requested for id="%s", rmember_me = %s' % (form.id_me.data, str(form.rem_me.data)))
		return redirect('/index')
	return render_template('login.html', title='sign In', form=form)
