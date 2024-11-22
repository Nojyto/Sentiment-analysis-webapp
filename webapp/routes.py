import pandas as pd
from flask import Blueprint, render_template, request, current_app
from webapp.models import db, PredictionLog

bp = Blueprint('app', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/predict', methods=['POST'])
def predict():
    studytime = float(request.form['studytime'])
    failures = int(request.form['failures'])
    absences = int(request.form['absences'])
    age = int(request.form['age'])
    g1 = int(request.form['g1'])

    input_data = pd.DataFrame({
        'studytime': [studytime],
        'failures': [failures],
        'absences': [absences],
        'age': [age],
        'G1': [g1]
    })
    predicted_grade = current_app.model.predict(input_data)[0]

    log_entry = PredictionLog(
        studytime=studytime,
        failures=failures,
        absences=absences,
        age=age,
        g1=g1,
        predicted_grade=predicted_grade
    )
    db.session.add(log_entry)
    db.session.commit()

    predicted_grade = max(0, predicted_grade)
    predicted_grade = min(20, predicted_grade)
    predicted_grade = round(predicted_grade, 2)

    return render_template('index.html',
                           prediction=predicted_grade,
                           form_values={
                               'studytime': studytime,
                               'failures': failures,
                               'absences': absences,
                               'age': age,
                               'g1': g1
                           })

@bp.route('/history', methods=['GET'])
def history():
    logs = PredictionLog.query.order_by(PredictionLog.timestamp.desc()).all()
    return render_template('history.html', logs=logs)
