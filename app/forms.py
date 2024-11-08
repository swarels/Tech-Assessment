from flask_wtf import FlaskForm 
from wtforms import StringField, DateTimeField
from wtforms.validators import InputRequired 

class AddShiftForm(FlaskForm): 
    name = StringField('Employee Name', validators=[InputRequired()])
    role = StringField('Role', validators=[InputRequired()])
    start_time = DateTimeField('Start Time', format='%Y-%m-%d %H:%M', validators=[InputRequired()])
    end_time = DateTimeField('End Time', format='%Y-%m-%d %H:%M', validators=[InputRequired()])