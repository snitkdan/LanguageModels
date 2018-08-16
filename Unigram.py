from LanguageModel import LanguageModel
from collections import Counter
import numpy as np


class Unigram(LanguageModel):

    def __init__(self, corpus_path=None):
        self.prob_table = None
        super(Unigram, self).__init__(corpus_path, 'UnigramModel')

    def predict(self, tokens):
        if self.prob_table:
            prob = 0.0
            for token in tokens:
                prob += np.log(self.prob_table[token])
            return prob
        return 0.0

    def train(self):
        if self.is_valid_corpus():
            self.prob_table = Counter()
            for s in open(self.corpus_path, 'r'):
                token = s.strip('\n').split(' ')
                self.prob_table.update(token)
            self.prob_table['stop'] = 1
            total = 1.0 * sum(self.prob_table.values())
            for k in self.prob_table:
                self.prob_table[k] /= total
