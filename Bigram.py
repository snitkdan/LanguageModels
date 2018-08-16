from Ngram import Ngram

class Bigram(Ngram):

    def __init__(self, corpus_path=None):
        super(Bigram, self).__init__(corpus_path, 'BigramModel')

    def get_token_gen(self, tokens):
        for i in range(len(tokens) - 1):
            yield (tokens[i], tokens[i+1])
