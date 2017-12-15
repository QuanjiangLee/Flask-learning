# flask学习笔记
---------------
## &emsp;&emsp;Flask是一个使用Python编写的轻量级Web应用框架。基于Werkzeug WSGI工具箱和Jinja2 模板引擎。Flask使用BSD授权。Flask被称为“microframework”，因为它使用简单的核心，用extension增加其他功能。Flask没有默认使用的数据库、窗体验证工具。然而，Flask保留了扩增的弹性，可以用Flask-extension加入这些功能：ORM、窗体验证工具、文件上传、各种开放式身份验证技术。
### 1.第一个Demo,"Hello, world"
- 1.1  环境需要：python2.7.12, pip9.0.1, sublime text3 
- 1.2  模块安装：pip install flask 
```python
from flask import Flask  #导入模块  
app = Flask(__name__)  #生成一个应用程序对象  
@app.route('/')  
def hello():  
	return 'hello,world'  
if __name__ == '__main__':  
	app.run(host='0.0.0.0', debug=True)
```

 - 1.3 flask 常用引用模块：    
 request, redirect, render_template  
 session escape  #escape模块提供字符串转义过滤  
 from flask import make_response #在视图里操纵上述步骤结果的响应对象，可以使用 make_response() 函数。 
 session.('a', xx)  #移除session a的信息  
 session.pop('a', xx)  #移除session a的信息  

 - 1.4 总结：  
 @app.route('URL') #定义URL路由  
 @app.route('URL<args>') #URL路由携带参数  
 with app.test_request_context() #创建一个request测试上下文环境  
 from flask import url_for #自定义构造url路由？  
 @app.errorhandler(404) #404 页面  

### 2.第二个Demo，templates模版使用  
- 2.1 在app目录下建立templates文件夹,在templates文件夹下建立相关html页面代码      
```
模版变量使用:{{  var }}  
逻辑嵌套：{{% if  %}}...{{ endif }}; {{% for i in var %}}...{{% endfor %}}  
模版公用继承：父模版:{{ %block content% }}{{%end block%}}; 子模版{% extends "base.html" %},{% block content %}...{% endblock %}  
模版包含：尚未练习。 
```
- 2.2 后台views接口传数据：     
```Python
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
    return render_template('posts.html', user=user, title=title, posts=posts)  #返回模版时传参
```
- 2.3 模版接收数据：
```Python
    {% for index in posts %}
    <div><p>{{ index.author.userName }} says: <strong>{{ index.message }}</strong></p></div> #模版接收并解析数据
    {% endfor %}
```
- 2.4 项目启动文件(microblog.py)：
```python
from app import app
app.run(host='0.0.0.0', debug=True)
```
运行:  
`` $ python microblog.py ``
### 3.第三个Demo,WTForms使用
- 3.1 使用config文件配置：
```
WTF_CSRF_ENABLED = True  #开启WTF csrf
SECRET_KEY = '\xc2es\xc2(9N\xb3\xfc\xe1\x95\x00@\xf1K[F\xd43\xc9y\x1d\\\x91'   #csrf 安全密钥使用os.urandom(24)生成。
在app文件夹下__init__.py中使用config文件
app.config.from_object('config')  #app configuration file
引用相关模块：
```
```python
from flask import render_template, flash, redirect #flash为善存模块
from flask_wtf import FlaskForm #flask_wtf需使用pip安装
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
class loginForm(FlaskForm):  #创建表单对象类
	id_me = StringField('id', validators=[DataRequired()])  
	rem_me = BooleanField('rem_me', default=False)
```
- 3.2 view部分代码：
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = loginForm()  #实例表单对象
	if form.validate_on_submit():   #form.validate_on_submit()为form是否提交验证
		flash('login requested for id="%s", rmember_me = %s' % (form.id_me.data, str(form.rem_me.data))) #使用flash接收消息
		return redirect('/index')
	return render_template('login.html', title='sign In', form=form)
```
```html
{% block content %}
	<script type="text/javascript">
	</script>
	<h1>Sign in</h1>
	<form action="" method="post" name="login">
	{{ form.hidden_tag() }} #影藏form对象标签
	<p>
		please enter your id:<br>
		{{ form.id_me(size=80) }}<br> #form 字段
	</p>
	<p>{{ form.rem_me }} Remember Me</p> #form 字段
	<p><input type="submit" name="Sign in"></p>
	</form>
{% endblock %}
```
- 3.3 使用闪取函数读取扁担数据：
```html
    	{% with messages = get_flashed_messages() %} #`get_flashed_messages()`获取表单提交后的flash闪存数据，据说获取完成后数据将不再存在。
    	{% if messages %}
    	<ul>
    		{% for m in messages %}
    			<li>{{ m }}</li> #列出闪取的数据
    		{% endfor %}
    	</ul>
    	{% endif %}
    	{% endwith %}
```
### 截至目前:工程目录树如下：


## python补充知识：  
`` 1 if a else 0  # 如果a==True返回1否则返回0 ``  
`` with fun() as f： # f为fun()返回值``

with 等价于：
```python
try:
    执行__enter__函数
    执行 with_block
finally:
    执行__exit__内容
```
python中的with的作用是自动释放对象，即使对象在使用的过程中有异常抛出。可以使用with的类型必须实现__enter__ __exit__。类似于try...finally,在finally中调用了释放函数。

## 扩展知识:Tornade Web框架
&emsp;&emsp;Tornado全称Tornado Web Server，是一个用Python语言写成的Web服务器兼Web应用框架，由FriendFeed公司在自己的网站FriendFeed中使用，被Facebook收购以后框架以开源软件形式开放给大众。
作为Web服务器，是一个轻量级的Web框架，Tornado有较为出色的抗负载能力，官方用nginx反向代理的方式部署Tornado和其它Python web应用框架进行对比，结果最大浏览量超过第二名近40%。
