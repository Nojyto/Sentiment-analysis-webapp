import os
import pickle
from flask import Flask
from webapp.models import db
from webapp.routes import bp as app_bp

def create_app():
    db_path = os.path.abspath("./webapp/instance/log.db")
    model_path = os.path.abspath("./webapp/instance/model.pkl")

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)
    app.register_blueprint(app_bp)
    with app.app_context():
        db.create_all()

    # Load ml model
    with open(model_path, 'rb') as f:
        app.model = pickle.load(f)

    return app
