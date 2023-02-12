import joblib
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/pos_clf.pkl", "rb") as f:
    model = joblib.load(f)


def features(sentence, index):
    # "sentence: [w1, w2, ...], index: the index of the word"
    return {
    'word': sentence[index],
    'is_first': index == 0,
    'is_last': index == len(sentence) - 1,
    'is_capitalized': sentence[index][0].upper() == sentence[index][0],
    'is_all_caps': sentence[index].upper() == sentence[index],
    'is_all_lower': sentence[index].lower() == sentence[index],
    'prefix-1': sentence[index][0],
    'prefix-2': sentence[index][:2],
    'prefix-3': sentence[index][:3],
    'suffix-1': sentence[index][-1],
    'suffix-2': sentence[index][-2:],
    'suffix-3': sentence[index][-3:],
    'prev_word': '' if index == 0 else sentence[index - 1],
    'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
    'has_hyphen': '-' in sentence[index],
    'is_numeric': sentence[index].isdigit(),
    'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }



def predict_pipeline(sentence):
    tagged_sentence = []
    tags = model.predict([features(sentence, index) for index in range(len(sentence))])
    return zip(sentence, tags)


def predict_pos(sentence):
    word_list = []
    POS_list = list(predict_pipeline(sentence=sentence.split()))
    for t in POS_list:
        word_list.append((str(t[0]),str(t[1])))
    return word_list
