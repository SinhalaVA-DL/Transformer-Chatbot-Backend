import tensorflow as tf
from .Sinhala_tokenizer import *
import re
from  .constants import *

class Predictor:

    def __init__(self,model,tokenizer):
        self.model =  model
        self.tokenizer = tokenizer

    def evaluate(self,sentence):
        sinhala_pre = SinhalaPreprocessor()
        START_TOKEN, END_TOKEN = [self.tokenizer.vocab_size], [self.tokenizer.vocab_size + 1]
        sentence = sinhala_pre.preprocess_sentence(sentence)

        sentence = tf.expand_dims(
            START_TOKEN + self.tokenizer.encode(sentence) + END_TOKEN, axis=0)

        output = tf.expand_dims(START_TOKEN, 0)

        for i in range(MAX_LENGTH):
            

            predictions = self.model(inputs=[sentence, output], training=False)

            # select the last word from the seq_len dimension
            predictions = predictions[:, -1:, :]
            predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

            # return the result if the predicted_id is equal to the end token
            if tf.equal(predicted_id, END_TOKEN[0]):
                break

            # concatenated the predicted_id to the output which is given to the decoder
            # as its input.
            output = tf.concat([output, predicted_id], axis=-1)

        return tf.squeeze(output, axis=0)


    def predict(self,sentence):
    # word_index = []
        prediction = self.evaluate(sentence).numpy()
        print(prediction)
        print(type(prediction))
        predicted_sentence = ''
        predicted_sentence = self.tokenizer.decode(
            [i for i in prediction if i < self.tokenizer.vocab_size])

        print('Input: {}'.format(sentence))
        print('Indexes: {}'.format(prediction))
        print('Output: {}'.format(predicted_sentence))

        return predicted_sentence



class SinhalaPreprocessor:

    @classmethod
    def preprocess_sentence(cls, sentence):
        # There are some &quote while the words
        sentence = re.sub(r"&quot", " ", sentence)
        # - and long hypen should replace with space
        sentence = re.sub(r"([\-–])", " ", sentence)
        # stripe "  සිංහල    භාෂාව " => " සිංහල භාෂාව "
        sentence = sentence.strip()
        # 40,000 -> 40000
        sentence = re.sub(r",000", r"000", sentence)
        # <u>නැගෙනහිර යුරෝපය</u> => නැගෙනහිර යුරෝපය U can be simple or capital
        # Here anything could be between the tag
        sentence = re.sub(r"(<.*?>)+(.*?)(<.*?>)*", r" \2 ", sentence)
        # Here I consider ? . ! , as single words
        sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
        # 100ක් -> 100 ක්
        sentence = re.sub(r"([\d]+)", r" \1 ", sentence)
        # remove `~@#$%^&*()_+=/><':;}{[]|\ “‘
        sentence = re.sub(r"([“‘`~@#$%^&*()_+=/><':;}{\[\]\\|])", "", sentence)
        # remove double quotes
        sentence = re.sub(r'[" "]+', " ", sentence)
        return sentence

    @classmethod
    def preprocess_sentences(cls, sentences):
        new_sentences = []
        for sentence in sentences:
            new_sentences.append(cls.preprocess_sentence(sentence))
        return new_sentences

# u([\u0D80-\u0DFF]+)u - to recognize sinhala words




