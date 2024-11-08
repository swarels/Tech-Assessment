from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Shift
from app.forms import AddShiftForm

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    shifts = Shift.query.all() 
    form = AddShiftForm()
    return render_template('index.html', shifts=shifts, form=form)

@main_routes.route('/add_shift', methods=['POST'])
def add_shift():    
    form = AddShiftForm()

    if form.validate_on_submit():
        name = form.name.data
        start_time = form.start_time.data
        end_time = form.end_time.data

        # Add a shift to the database 
    
    return redirect(url_for('main.index'))

@main_routes.route('/delete_shift', methods=['POST'])
def delete_shift():
    # Delete a shift from the database
    
    return redirect(url_for('main.index'))

@main_routes.route('/edit_shift', methods=['POST'])
def edit_shift():
    # Edit a shift in the database
    
    return redirect(url_for('main.index'))