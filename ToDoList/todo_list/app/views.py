from flask import render_template, flash, request, redirect, url_for
from app import app, db, models
from .forms import TaskForm
from .models import Task #- uncommented gives error __init__ takes one argument was given two
							#and changes text fields for filling in addtask for 'None'

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/addtask', methods=['GET', 'POST'])
def addtask():
	# task = Task(request.form['date'], request.form['title'], request.form['describe'], request.form['complete'])
	# db.session.add(task) #adding task to database
	# db.session.commit() #saving task in database
	form=TaskForm()
	if form.validate_on_submit():
		print(form.validate_on_submit())
		t = Task(date=form.date.data, title=form.title.data, describe=form.describe.data, complete=False)
		db.session.add(t) #adding task to database #uncommented gives db not defined error
		db.session.commit() #saving task in database
		#it doesn't seem to be adding stuff...
		return redirect(url_for('home'))

	return render_template("addtask.html", title='Create a new task', form=form)

@app.route('/complete', methods=['GET', 'POST'])
def complete():
	task = models.Task.query.filter_by(complete=True).all()
	return render_template("complete.html", title='Complete Tasks', task=task) #, task=task)

@app.route('/incomplete', methods=['GET', 'POST'])
def incomplete():
	task = models.Task.query.filter_by(complete=False).all()
	return render_template("incomplete.html", title='Incomplete Tasks', task=task) #, task=task)

#for marking as complete
@app.route('/incomplete/<id>', methods=['GET', 'POST'])
def markcomplete(id):
	task = models.Task.query.filter_by(id=int(id)).first()
	task.complete=True
	db.session.commit()
	return redirect(url_for('complete'))


#if __name__=="__main__"
	#app.run(debug=True)
