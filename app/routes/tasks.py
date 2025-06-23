# # from flask import Blueprint, render_template, request, redirect, url_for, flash, session
# # from app import db
# # from app.models import Task

# # tasks_bp = Blueprint('tasks', __name__)

# # @tasks_bp.route('/')
# # def view_tasks():
# #     if 'user'not in session:
# #         return redirect(url_for('auth.login'))
    
# #     tasks = Task.query.all()
# #     return render_template('tasks.html', tasks = tasks)

# # @tasks_bp.route('/add', methods=["POST"])
# # def add_task():
# #     if 'user' not in session:
# #         return redirect(url_for('auth.login'))
    
# #     title = request.form.get('title')
# #     if title:
# #         new_task = Task(title=title, status="Pending")
# #         db.session.add(new_task)
# #         db.session.commit()
# #         flash('Task Added successfully', 'success')

# #     return redirect(url_for('tasks.view_tasks'))

# # @tasks_bp.route('/toggle/<int:task_id', methods=["POST"])
# # def toggle_status(task_id):
# #     task = task.query.get(task_id)
# #     if task:
# #         if task.status == 'Pending':
# #             task.status = 'Working'
# #         elif task.status == 'Working':
# #             task.status = 'Done'
# #         else:
# #             task.status = 'Pending'
# #         db.session.commit()
# #     return redirect(url_for('tasks.view_tasks'))

# # @tasks_bp.route('/clear', methods=['POST'])
# # def clear_tasks():
# #     Task.query.delete()
# #     db.session.commit()
# #     flash('All tasks cleared', 'info')
# #     return redirect(url_for('tasks.view_tasks'))


# from flask import Blueprint, render_template, request, redirect, url_for, flash, session
# from app import db
# from app.models import Task

# tasks_bp = Blueprint('tasks', __name__)

# # ---------------------- Home Route ----------------------
# @tasks_bp.route('/')
# def view_tasks():
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))
    
#     tasks = Task.query.all()
#     return render_template('tasks.html', tasks=tasks)

# # ---------------------- Add Task ----------------------
# @tasks_bp.route('/add', methods=["POST"]) 
# def add_task():
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))
    
#     title = request.form.get('title')
#     if title:
#         new_task = Task(title=title, status="Pending")
#         db.session.add(new_task)
#         db.session.commit()
#         flash('Task added successfully', 'success')

#     return redirect(url_for('tasks.view_tasks'))

# # ---------------------- Toggle Task Status ----------------------
# @tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])  # ✅ fixed: angle bracket and method
# def toggle_status(task_id):
#     task = Task.query.get(task_id)  # ✅ fixed: use Task not task
#     if task:
#         if task.status == 'Pending':
#             task.status = 'Working'
#         elif task.status == 'Working':
#             task.status = 'Done'
#         else:
#             task.status = 'Pending'
#         db.session.commit()
#     return redirect(url_for('tasks.view_tasks'))

# # ---------------------- Clear All Tasks ----------------------
# @tasks_bp.route('/clear', methods=["POST"])
# def clear_tasks():
#     Task.query.delete()
#     db.session.commit()
#     flash('All tasks cleared', 'info')
#     return redirect(url_for('tasks.view_tasks'))

# # ---------------------- Delete Individual Task ----------------------
# @tasks_bp.route('/delete/<int:task_id>', methods=["POST"])
# def delete_task(task_id):
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))

#     task = Task.query.get_or_404(task_id)
#     db.session.delete(task)
#     db.session.commit()
#     flash('Task deleted successfully', 'danger')
#     return redirect(url_for('tasks.view_tasks'))

# from flask import Blueprint, render_template, request, redirect, url_for, flash, session
# from app import db
# from app.models import Task, User 
# from datetime import datetime


# tasks_bp = Blueprint('tasks', __name__)

# @tasks_bp.route('/')
# def view_tasks():
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))

#     current_user = User.query.filter_by(username=session['user']).first()
#     tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.start_time.asc()).all()

#     return render_template('tasks.html', tasks=tasks)


# @tasks_bp.route('/add', methods=["POST"])
# def add_task():
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))

#     title = request.form.get('title')
#     start_time_str = request.form.get('start_time')
#     end_time_str = request.form.get('end_time')

#     start_time = datetime.strptime(start_time_str, '%H:%M').time() if start_time_str else None
#     end_time = datetime.strptime(end_time_str, '%H:%M').time() if end_time_str else None

#     current_user = User.query.filter_by(username=session['user']).first()

#     if title:
#         new_task = Task(
#             title=title,
#             status="Pending",
#             start_time=start_time,
#             end_time=end_time,
#             user_id=current_user.id  # ✅ Link task to user
#         )
#         db.session.add(new_task)
#         db.session.commit()
#         flash('Task added successfully', 'success')

#     return redirect(url_for('tasks.view_tasks'))


# @tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
# def toggle_status(task_id):
#     task = Task.query.get(task_id)
#     if task:
#         if task.status == 'Pending':
#             task.status = 'Working'
#         elif task.status == 'Working':
#             task.status = 'Done'
#         else:
#             task.status = 'Pending'
#         db.session.commit()
#     return redirect(url_for('tasks.view_tasks'))

# @tasks_bp.route('/clear', methods=["POST"])
# def clear_tasks():
#     Task.query.delete()
#     db.session.commit()
#     flash('All tasks cleared', 'info')
#     return redirect(url_for('tasks.view_tasks'))

# @tasks_bp.route('/delete/<int:task_id>', methods=["POST"])
# def delete_task(task_id):
#     if 'user' not in session:
#         return redirect(url_for('auth.login'))

#     task = Task.query.get_or_404(task_id)
#     db.session.delete(task)
#     db.session.commit()
#     flash('Task deleted successfully', 'danger')
#     return redirect(url_for('tasks.view_tasks'))

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from app import db
from app.models import Task, User

tasks_bp = Blueprint('tasks', __name__)


# View all tasks of the logged-in user
@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    current_user = User.query.filter_by(username=session['user']).first()
    if not current_user:
        flash('User not found. Please log in again.', 'danger')
        return redirect(url_for('auth.login'))

    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.start_time.asc()).all()
    return render_template('tasks.html', tasks=tasks)


# Add a new task for the logged-in user
@tasks_bp.route('/add', methods=["POST"])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    start_time_str = request.form.get('start_time')
    end_time_str = request.form.get('end_time')

    start_time = datetime.strptime(start_time_str, '%H:%M').time() if start_time_str else None
    end_time = datetime.strptime(end_time_str, '%H:%M').time() if end_time_str else None

    current_user = User.query.filter_by(username=session['user']).first()

    if title:
        new_task = Task(
            title=title,
            status="Pending",
            start_time=start_time,
            end_time=end_time,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully.', 'success')
    else:
        flash('Title is required to add a task.', 'warning')

    return redirect(url_for('tasks.view_tasks'))


# Toggle status between Pending → Working → Done → Pending
@tasks_bp.route('/toggle/<int:task_id>', methods=["POST"])
def toggle_status(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)

    if task.status == 'Pending':
        task.status = 'Working'
    elif task.status == 'Working':
        task.status = 'Done'
    else:
        task.status = 'Pending'

    db.session.commit()
    flash('Task status updated.', 'info')
    return redirect(url_for('tasks.view_tasks'))


# Delete a specific task
@tasks_bp.route('/delete/<int:task_id>', methods=["POST"])
def delete_task(task_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully.', 'danger')
    return redirect(url_for('tasks.view_tasks'))


# Clear all tasks (only for the logged-in user)
@tasks_bp.route('/clear', methods=["POST"])
def clear_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))

    current_user = User.query.filter_by(username=session['user']).first()
    Task.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('All your tasks have been cleared.', 'info')
    return redirect(url_for('tasks.view_tasks'))
