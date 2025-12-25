import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in a text
    :param text_to_analyze: the text to detect the emotions 
    :returns: the dominant emotion and scores form 0 to 1 for all the emotions
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = input_json, headers=header)

    result = {}
    if response.status_code == 200:
        formatted_content = json.loads(response.text)
        predictions_data = formatted_content["emotionPredictions"][0]
        emotions = predictions_data["emotion"]

        # the param "key=emotions.get" sets the comparison criteria as  
        # the value and not the key of the dictionary elements
        max_emotion = max(emotions, key=emotions.get)
    
        result = emotions.copy()
        result["dominant_emotion"] = max_emotion

    elif response.status_code == 400:
        result["anger"] = None
        result["disgust"] = None
        result["fear"] = None
        result["joy"] = None
        result["sadness"] = None
        result["dominant_emotion"] = None

    return result
