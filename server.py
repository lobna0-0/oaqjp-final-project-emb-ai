"""Flask server for Emotion Detection"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/")
def home():
    """
    Render the main HTML homepage.
    """
    return render_template("index.html")
@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Route to detect emotion from the provided text using emotion_detector function.
    Returns a formatted string with emotion scores or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    print("DEBUG:", result)
    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return response
if __name__ == "__main__":
    app.run(debug=True)
