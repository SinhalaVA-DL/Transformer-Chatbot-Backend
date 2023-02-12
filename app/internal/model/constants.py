
ATTEMPT = 1
# Maximum sentence length
MAX_LENGTH = 20

# Maximum number of samples to preprocess
MAX_SAMPLES = 70000 # 0 = for All of data otherwise mention the size

# Cut off value of words in the dictionary
TRESHOLD_VALUE = 1

# For tf.data.Dataset
BATCH_SIZE = 8 
BUFFER_SIZE = 20000 #Shuffle data in the dataset

# For Transformer
NUM_LAYERS = 2
D_MODEL = 512
NUM_HEADS = 16
UNITS = 512
DROPOUT = 0.3

EPOCHS = 2
TRAINING_RATIO = 0.9