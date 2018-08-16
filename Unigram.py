from Ngram import Ngram

class Unigram(Ngram):

    def __init__(self, corpus_path=None):
        super(Unigram, self).__init__(corpus_path, 'UnigramModel')

    def get_token_gen(self, tokens):
        for t in tokens:
            yield t
