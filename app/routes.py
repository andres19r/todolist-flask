from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import CreateTaskForm
from app.models import Task


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

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
