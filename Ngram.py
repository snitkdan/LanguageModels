from LanguageModel import LanguageModel
from collections import Counter
import numpy as np

class Ngram(LanguageModel):

    def __init__(self, corpus_path=None, model_name=None):
        self.prob_table = None
        self.count_table = None
        super(Ngram, self).__init__(corpus_path, model_name)

    def predict(self, tokens):
        if self.prob_table:
            prob = 0.0
            for token in self.get_token_gen(tokens):
                prob += np.log(self.prob_table[token])
            return prob
        return 0.0

    def train(self):
        if self.is_valid_corpus():
            self.prob_table = Counter()
            self.count_table = Counter()
            total = 0.0
            for s in open(self.corpus_path, 'r'):
                for token in self.get_token_gen(s.strip('\n').split(' ')):
                    total += 1
                    self.count_table.update([token])
                    self.prob_table.update([token])
            self.normalize(total, self.prob_table)