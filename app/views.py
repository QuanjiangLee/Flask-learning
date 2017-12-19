# coding=UTF-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, LoginMa
from forms import loginForm
from models import UserInf


@app.before_request
def before_request():
    g.user = current_user  
    print(g.user)

@LoginMa.user_loader
def load_User(userId):
    return UserInf.query.get(int(userId))

@app.route('/', methods=['GET', 'POST'])
def root():
    form = loginForm()
    return render_template('login.html', title='sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():                   
        userName = request.form.get('userName', '')
        passWord = request.form.get('passWord', '')
        rem_me = request.form.get('rem_me', False)
        print(userName, passWord, '--------')
        user = UserInf.query.filter_by(userName = userName).first()
        if  not user  or user.userPassword != passWord:
            flash("userName or password is invalid!")
            return render_template('login.html', title='sign In', form=form)
        else:
            login_user(user, remember=rem_me)
            flash("login is successful!")
            return redirect(request.args.get('next') or url_for('index'))
        #flash('login requested for id="%s", rmember_me = %s' % (form.id_me.data, str(form.rem_me.data)))
        #return redirect('/index')
    else:
        flash("userName or password is not null!")
    return render_template('login.html', title='sign In', form=form)

'''
@Oid.after_login
def after_login(resp):
    if resp.userEmail is None or resp.userEmail == "":
        flash('Invalid login!!!')
        return redirect(url_for('login'))
    user = UserInf.query.filter_by(userEmail = resp.email).first()
    if user is None:            #如果用户不存在就创建一个登录
        userName = resp.userName
        if userName is None or userName == "":
            userName = resp.userEmail.split('@')[0]  
            user = UserInf(userName=userName, userEmail=resp.email)
        db.session.add(user)
        db.session.commit()
    rem_me = False
    if 'rem_me' in session:
        rem_me = session['rem_me']
        session.pop('rem_me', None)
    login_user(user, rem_me = rem_me)
    return redirect( url_for('index')) #重定向到下一个url或主页
'''

@app.route('/logout')
@login_required
def logout():
    form = loginForm()
    logout_user()
    return redirect('/')


@app.route('/index', methods=['GET','POST'])
@login_required
def index():
    user = g.user
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