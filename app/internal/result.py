import random
import json
import pickle
import numpy as np
from .model.chatbot import predictor
from .functions.functions import *
from pathlib import Path
from tensorflow import keras

BASE_DIR = Path(__file__).resolve(strict=True).parent


intents = json.loads(open(f"{BASE_DIR}/data/intents.json", encoding="utf8").read())

words = pickle.load(open(f"{BASE_DIR}/data/words.pkl", 'rb'))
classes = pickle.load(open(f"{BASE_DIR}/data/classes.pkl", 'rb'))
model = keras.models.load_model(f"{BASE_DIR}/data/chatbot_model.h5")

def clean_up_sentence(sentence):
    sentence_words = sentence.split()
    sentence_words = [word.lower() for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
    return(np.array(bag))

def predict_class(sentence):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list




def get_result(question:str):
    results = predict_class(question)
    tag = results[0]['intent']
    proberbility = results[0]['probability']
    if float(proberbility) == 1:
        list_of_intents = intents['intents']
        for i in list_of_intents:
            if(i['tag'] == tag):
                if i['has_function']:
                    result = get_func[tag]()
                else:
                    result = random.choice(i['responses'])
                break
        return result
    else:
        result = predictor.predict(question)
        return result

