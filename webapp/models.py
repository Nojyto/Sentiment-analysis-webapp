from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PredictionLog(db.Model):
    __tablename__ = 'prediction_log'
    id = db.Column(db.Integer, primary_key=True)
    text_input = db.Column(db.String, nullable=False)
    predicted_sentiment = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())