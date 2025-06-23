from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# 🔁 define globally, not inside app
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(tasks_bp)

    app.register_blueprint(auth_bp, url_prefix='/auth')   # 👈 Add this
    app.register_blueprint(tasks_bp)  # leave this as it is

    return app

