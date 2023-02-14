import tensorflow as tf
import re
from .Predictor import *
from .Sinhala_tokenizer import *
from .Transformer import CustomSchedule, transformer, loss_function
from pathlib import Path


BASE_DIR = Path(__file__).resolve(strict=True).parent


tokenizer_file = open(f"{BASE_DIR}/tokenizer.pkl", "rb") 
# weights_file = open(f"{BASE_DIR}/weights.h5", "rb") 

tokenizer = SinhalaTokenizer()
tokenizer.create_data_using_pickle_file(tokenizer_file)
VOCAB_SIZE = tokenizer.vocab_size + 2


# clear backend
tf.keras.backend.clear_session()

learning_rate = CustomSchedule(D_MODEL)

optimizer = tf.keras.optimizers.Adam(
    learning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)

def accuracy(y_true, y_pred):
  # ensure labels have shape (batch_size, MAX_LENGTH - 1)
  y_true = tf.reshape(y_true, shape=(-1, MAX_LENGTH - 1))
  return tf.keras.metrics.sparse_categorical_accuracy(y_true, y_pred)

# initialize and compile model within strategy scope

model = transformer(
      vocab_size=VOCAB_SIZE,
      num_layers=NUM_LAYERS,
      units=UNITS,
      d_model=D_MODEL,
      num_heads=NUM_HEADS,
      dropout=DROPOUT)  

model.compile(optimizer=optimizer, loss=loss_function, metrics=[accuracy])
model.load_weights(f"{BASE_DIR}/weights.h5")

predictor = Predictor(model, tokenizer)




