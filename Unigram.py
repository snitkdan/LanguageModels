from Ngram import Ngram
from random import choice

class Unigram(Ngram):

    def __init__(self, corpus_path=None):
        super(Unigram, self).__init__(corpus_path, 'UnigramModel')

    def get_token_gen(self, tokens):
        for t in tokens:
            yield t
        yield 'STOP'

    def generate_sentence(self):
        if self.count_table:
            sentence = []
            next_token = choice(list(self.count_table.elements()))
            while next_token != 'STOP':
                sentence.append(next_token)
                next_token = choice(list(self.count_table.elements()))
            return ' '.join(sentence)
        return ''

