"""Executing this function initiates an application of emotion detections. Executed with
Flask on localhost:5000
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """This code receives text from the HTML interface and runs emotion detector library 
    to obtain the sentiment analysis. The output returned shows the setiment scores
    and the dominant sentiment of the received text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)

    if emotions["dominant_emotion"] is None:
        return "<b> Invalid text! Please try again!</b>"

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]
    dominant = emotions["dominant_emotion"]

    response_message = f"For the given statement, the system \
    response is 'anger': {anger}, 'disgust': {disgust}, \
    'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. \
    The dominant emotion is <b>{dominant}</b>."

    return response_message

@app.route("/")
def render_index_page():
    """ This function renders the main application page """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
