from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class CreateTaskForm(FlaskForm):
    name = StringField('Task', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Create')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')
