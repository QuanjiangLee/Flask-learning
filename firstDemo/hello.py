from flask import Flask, url_for, request, redirect, render_template
app = Flask(__name__)



@app.route('/')
def hello():
	return 'hello,world'

@app.route('/user/<userName>')
def hello_user(userName):
	return 'hello, %s' % userName

@app.route('/num/<int:num>')
def show_num(num):
	return 'number is %d' % num

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'POST'
	else:
		print 'requre to GET method'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

with app.test_request_context():
	print url_for('user', userName = 'Quanjiang')

