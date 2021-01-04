from flask_wtf import Form
from wtforms import DateField, TextField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(Form):
	date = DateField('date',format='%d-%m-%Y', validators=[DataRequired()])
	title = TextField('title', validators=[DataRequired()])
	describe = TextField('describe', validators=[DataRequired()])
	complete = BooleanField('complete'); #should state False at the beginning
