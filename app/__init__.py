from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' 
    app.config['SECRET_KEY'] = 'can you keep a secret?'

    db.init_app(app)

    from app.routes import main_routes
    app.register_blueprint(main_routes)

    return app
