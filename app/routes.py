from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Shift

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    shifts = Shift.query.all() 
    return render_template('index.html', shifts=shifts)

@main_routes.route('/add_shift', methods=['POST'])
def add_shift():    
    # Add a shift to the database (ensure that it does not clash with an existing shift for that employee in the database)
    
    return redirect(url_for('main.index'))

@main_routes.route('/delete_shift', methods=['POST'])
def delete_shift():
    # Delete a shift from the database
    
    return redirect(url_for('main.index'))

@main_routes.route('/edit_shift', methods=['POST'])
def edit_shift():
    # Edit a shift in the database
    
    return redirect(url_for('main.index'))