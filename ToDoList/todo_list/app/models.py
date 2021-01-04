from app import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True) #our primary key
	date = db.Column(db.DateTime)
	title = db.Column(db.String(200), index=True, unique=True) #title of task
	describe = db.Column(db.String(1000), index=True, unique=True) #task descibtion
	complete = db.Column(db.Boolean);
	#duration = db.Column(db.Integer)
	#rent = db.Column(db.Float)
