from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import CreateTaskForm, EmptyForm
from app.models import Task


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    tasks = Task.query.filter_by(status=False) \
            .order_by(Task.created.desc()) \
            .paginate(page, app.config['TASKS_PER_PAGE'], False)
    next_url = url_for('index', page=tasks.next_num) \
        if tasks.has_next else None
    prev_url = url_for('index', page=tasks.prev_num) \
        if tasks.has_prev else None
    form = EmptyForm()
    return render_template('index.html', tasks=tasks.items, form=form,
                           next_url=next_url, prev_url=prev_url)

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

@app.route('/completed_tasks')
def completed_tasks():
    page = request.args.get('page', 1, type=int)
    tasks = Task.query.filter_by(status=True) \
            .order_by(Task.completed.desc()) \
            .paginate(page, app.config['TASKS_PER_PAGE'], False)
    next_url = url_for('index', page=tasks.next_num) \
        if tasks.has_next else None
    prev_url = url_for('index', page=tasks.prev_num) \
        if tasks.has_prev else None
    return render_template('index.html', tasks=tasks.items,
                           next_url=next_url, prev_url=prev_url)
