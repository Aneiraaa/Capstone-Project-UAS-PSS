from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql  # Import pymysql directly

# Allow PyMySQL to be used as MySQLdb
pymysql.install_as_MySQLdb()

# Initialize the database and migration objects
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Load configuration from config.py

    # Initialize the database and migration with the app
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes import app as routes_blueprint  # Import routes
        app.register_blueprint(routes_blueprint)  # Register the blueprint
        db.create_all()  # Create database tables if they don't exist

    return app