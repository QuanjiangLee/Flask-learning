from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
	id_me = StringField('id', validators=[DataRequired()])
	rem_me = BooleanField('rem_me', default=False)
