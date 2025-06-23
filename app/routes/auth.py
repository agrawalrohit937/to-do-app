# from flask import Blueprint, render_template, request, redirect, url_for, flash, session
# auth_bp = Blueprint('auth', __name__)

# USER_CREDENTIALS = {
#     'username': 'admin',
#     'password': '1234'
# }

# @auth_bp.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get('username')
#         password = request.form.get('password')

#         if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
#             session['user'] = username
#             flash('Login Succssful', 'success')
#             return redirect(url_for('tasks.view_tasks'))
#         else:
#             flash('Invalid username or password', 'danger')
#             return redirect(url_for('auth.login'))

#     return render_template('login.html')

# @auth_bp.route('/logout')
# def logout():
#     session.pop('user', None)
#     flash('Logged out', 'info')
#     return redirect(url_for('auth.login'))
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import User  # Ensure this exists

auth_bp = Blueprint('auth', __name__)

# ✅ Fix 1: Redirect "/" depending on login status
@auth_bp.route('/')
def home_redirect():
    if 'user' in session:
        return redirect(url_for('tasks.view_tasks'))
    else:
        return redirect(url_for('auth.login'))


# ✅ Fix 2: Correct spelling of template + optional auto-login
@auth_bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists!", "danger")
            return redirect(url_for('auth.register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # ✅ Optional: Auto login
        session['user'] = new_user.username
        flash("Registration successful. Welcome!", "success")
        return redirect(url_for('tasks.view_tasks'))

    return render_template("registeration.html")  # ✅ spelling fixed


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user'] = user.username
            flash("Login successful", "success")
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for('auth.login'))

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully", "info")
    return redirect(url_for('auth.login'))
