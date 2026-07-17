from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders the main application page."""
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Receives text from the frontend, analyzes the emotions using
    the EmotionDetection package, and returns a formatted string.
    """
    # Grab the text argument sent from the frontend script
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion detector function
    response = emotion_detector(text_to_analyze)
    
    # Extract values from the response dictionary
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Return the exact response string format requested by the customer
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)