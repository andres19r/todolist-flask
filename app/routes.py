from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import CreateTaskForm, EmptyForm
from app.models import Task


@app.route('/')
def index():
    tasks = Task.query.all()
    form = EmptyForm()
    return render_template('index.html', tasks=tasks, form=form)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateTaskForm()
    if form.validate_on_submit():
        task = Task(name=form.name.data, description=form.description.data)
        db.session.add(task)
        db.session.commit()
        flash('Task created')
        return redirect(url_for('index'))
    return render_template('create.html', title='Create Task', form=form) 

@app.route('/complete/<task>', methods=['GET', 'POST'])
def complete(task):
    form = EmptyForm()
    if form.validate_on_submit():
        task = Task.query.filter_by(name=task).first()
        if task is None:
            flash(f"Task {task} not found.")
            return redirect(url_for('index'))
        task.complete_task()
        db.session.commit()
        flash('You have completed the task!')
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
