from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    tasks = db.relationship('Task', backref='user', lazy=True)  # 👈 One-to-many

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Pending")
    start_time = db.Column(db.Time, nullable=True)
    end_time = db.Column(db.Time, nullable=True)
    
    # ✅ Link to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
