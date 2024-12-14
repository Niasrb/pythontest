from flask import Flask
from config import Config
from .database import db
from .routes import main

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialisation des extensions
    db.init_app(app)

    # Enregistrement des blueprints
    app.register_blueprint(main)

    # Création des tables
    with app.app_context():
        db.create_all()

    return app