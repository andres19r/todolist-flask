from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import CreateTaskForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateTaskForm()
    if form.validate_on_submit():
        flash('Task created')
        return redirect(url_for('index'))
    return render_template('create.html', title='Create Task', form=form)
