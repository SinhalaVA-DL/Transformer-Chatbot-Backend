import json
import pickle


class SinhalaTokenizer:
    def __init__(self):
        self.sentence2int = {}
        self.int2word = {}
        self.vocab_size = 0


    def build_dictionaries(self, s , threshold_val):
        # count each unique words
        word2count = {}
        for sentence in s:
            for word in sentence.split():
                if word not in word2count:
                    word2count[word] = 1
                else:
                    word2count[word] += 1

        # take equal or above count according to the threshold value
        threshold_value = threshold_val
        self.sentence2int = {}
        word_number = 0

        # adding tokens
        tokens = ['<PAD>', '<EOS>', '<OUT>', '<SOS>']
        for token in tokens:
            self.sentence2int[token] = len(self.sentence2int) + 1
            word_number += 1

        # tokenizing word
        for word, count in word2count.items():
            if count >= threshold_value:
                self.sentence2int[word] = word_number
                word_number += 1

        self.vocab_size = word_number

        # Creating the inverse dictionary of the sentence2int dictionary
        self.int2word = {w_i: w for w, w_i in self.sentence2int.items()}

        # return tokenized sentences
        sentences_into_int = []
        for sentence in s:
            ints = []
            for word in sentence.split():
                if word not in self.sentence2int:
                    ints.append(self.sentence2int['<OUT>'])
                else:
                    ints.append(self.sentence2int[word])
            sentences_into_int.append(ints)
        # print(self.int2word)

    def encode(self, sentence):
        # return tokenized sentences
        ints = []
        for word in sentence.split():
            if word not in self.sentence2int:
                ints.append(self.sentence2int['<OUT>'])
            else:
                ints.append(self.sentence2int[word])
        return ints

    def decode(self, ints):
        sentence = ''
        for i in ints:
            if i not in self.int2word:
                sentence = sentence + ' ' + self.int2word['<OUT>']
            else:
                sentence = sentence + ' ' + self.int2word[i]
        return sentence

    def save_data_to_pickle_file(self, name):
        f = open(name, "wb")
        pickle.dump([self.int2word, self.sentence2int], f)
        # close file
        f.close()

    def create_data_using_pickle_file(self, f):
        self.int2word, self.sentence2int = pickle.load(f)
        self.vocab_size = len(self.sentence2int)

    def save_sinhala_words_to_txt(self):
        with open('Sinhala_dictionary.txt', 'w', encoding='utf-8') as convert_file:
            convert_file.write(json.dumps(self.sentence2int, ensure_ascii=False, indent=4, sort_keys=True))