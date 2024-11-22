from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PredictionLog(db.Model):
    __tablename__ = 'prediction_log'
    id = db.Column(db.Integer, primary_key=True)
    studytime = db.Column(db.Float, nullable=False)
    failures = db.Column(db.Integer, nullable=False)
    absences = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    g1 = db.Column(db.Integer, nullable=False)
    predicted_grade = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
