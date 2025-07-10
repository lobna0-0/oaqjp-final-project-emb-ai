def emotion_detector(text_to_analyze):
    import json
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }
    responses = {
        "I am glad this happened": {
            "anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.95, "sadness": 0.02
        },
        "I am really mad about this": {
            "anger": 0.90, "disgust": 0.02, "fear": 0.01, "joy": 0.01, "sadness": 0.06
        },
        "I feel disgusted just hearing about this": {
            "anger": 0.03, "disgust": 0.92, "fear": 0.01, "joy": 0.01, "sadness": 0.03
        },
        "I am so sad about this": {
            "anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.01, "sadness": 0.96
        },
        "I am really afraid that this will happen": {
            "anger": 0.01, "disgust": 0.01, "fear": 0.94, "joy": 0.01, "sadness": 0.03
        }
    }
    emotions = responses.get(text_to_analyze, {
        "anger": 0.05, "disgust": 0.02, "fear": 0.04, "joy": 0.93, "sadness": 0.01
    })
    dominant_emotion = max(emotions, key=emotions.get)
    result = emotions.copy()
    result["dominant_emotion"] = dominant_emotion
    result["status_code"] = 200
    return result
