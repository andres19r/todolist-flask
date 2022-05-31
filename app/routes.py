from app import app
from flask import render_template
from app.forms import CreateTaskForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    form = CreateTaskForm()
    return render_template('create.html', title='Create Task', form=form)
