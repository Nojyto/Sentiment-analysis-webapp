import os ; os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import pickle
from flask import Flask
from webapp.models import db
from webapp.routes import bp as app_bp
from tensorflow.keras.models import load_model

def create_app():
    db_path = os.path.abspath("./webapp/instance/log.db")
    model_path = os.path.abspath("./webapp/instance/sentiment_analysis_nn_model.keras")
    tokenizer_path = os.path.abspath("./webapp/instance/tokenizer.pkl")

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)
    app.register_blueprint(app_bp)
    with app.app_context():
        db.create_all()

    # Load neural network model and tokenizer
    app.model = load_model(model_path, compile=False)
    with open(tokenizer_path, 'rb') as f:
        app.tokenizer = pickle.load(f)
    app.label_map = {'negative': 0, 'neutral': 1, 'positive': 2}

    return app
