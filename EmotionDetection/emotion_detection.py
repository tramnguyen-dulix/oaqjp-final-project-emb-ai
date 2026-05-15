import requests 
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    # URL of the sentiment analysis service 
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Set the headers required for the API request 
    response = requests.post(url, json=myobj, headers=header) 
    formatted_response = json.loads(response.text)
    emotion = formatted_response["emotionPredictions"][0]["emotion"]
    # Format for the response
    # this finds the key (e.g., 'joy') with the highest value (e.g., 0.96)
    dominant_emotion = max(emotion, key=emotion.get)
        
    # Add the dominant emotion to your output dictionary
    emotion['dominant_emotion'] = dominant_emotion
    return emotion
    # Return the response