import random
import json
import pickle
import numpy as np
from tensorflow import keras
import sinhala_preprocessor as preprocesser
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent


def sinhala_splitter(words):
    return words.split(" ")


intents = json.loads(open(f'{BASE_DIR}/intents.json', encoding="utf8").read())

words = []
classes = []
documents = []
prepocessor = preprocesser.SinhalaPreprocessor()


for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word
        w = sinhala_splitter(prepocessor.preprocess_sentence(pattern))
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


words = sorted(set(words))
classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    word_patterns = doc[0]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)

train_x = list(training[:, 0])
train_y = list(training[:, 1])

model = keras.Sequential()
model.add(keras.layers.Dense(128, input_shape=(
    len(train_x[0]),), activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(len(train_y[0]), activation='softmax'))

sgd = keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y),
                 epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)
print("done")
