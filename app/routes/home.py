from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))
    return render_template('index.html')
