from flask import Blueprint, render_template, request, current_app
from webapp.models import db, PredictionLog
from tensorflow.keras.preprocessing.sequence import pad_sequences

bp = Blueprint('app', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/predict', methods=['POST'])
def predict():
    text_input = request.form['text_input']

    # Preprocess input text using tokenizer
    tokenizer = current_app.tokenizer
    max_sequence_length = 100
    text_seq = tokenizer.texts_to_sequences([text_input])
    text_pad = pad_sequences(text_seq, maxlen=max_sequence_length, padding='post')

    # Predict sentiment using the neural network model
    model = current_app.model
    prediction = model.predict(text_pad)
    predicted_sentiment = list(current_app.label_map.keys())[prediction.argmax(axis=1)[0]]

    # Log prediction
    log_entry = PredictionLog(
        text_input=text_input,
        predicted_sentiment=predicted_sentiment
    )
    db.session.add(log_entry)
    db.session.commit()

    return render_template('index.html', prediction=predicted_sentiment, form_values={'text_input': text_input})

@bp.route('/history', methods=['GET'])
def history():
    logs = PredictionLog.query.order_by(PredictionLog.timestamp.desc()).all()
    return render_template('history.html', logs=logs)
