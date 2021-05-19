from flask import jsonify

from main.app import app
from main.engines import evaluate_text
from main.engines.translate import translate_to_training_language
from main.schemas.prediction import PredictionResultSchema, PredictSentimentSchema
from main.utils import parse_args_with


@app.route("/sentiments/predict", methods=["POST"])
@parse_args_with(PredictSentimentSchema())
def predict_sentiment(args):
    text = args["text"]
    translated_text = translate_to_training_language(text)
    prediction = evaluate_text(translated_text)

    return jsonify(PredictionResultSchema().dump(prediction))
