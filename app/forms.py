from flask_wtf import FlaskForm 
from wtforms import StringField, DateTimeField
from wtforms.validators import InputRequired 

class AddShiftForm(FlaskForm): 
    name = StringField('Employee Name', validators=[InputRequired()])
    start_time = DateTimeField('Start Time', validators=[InputRequired()])
    end_time = DateTimeField('End Time', validators=[InputRequired()])