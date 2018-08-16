from LanguageModel import LanguageModel
from collections import Counter


class EmpiricalDistribution(LanguageModel):

    def __init__(self, corpus_path=None):
        self.prob_table = None
        super(EmpiricalDistribution, self).__init__(corpus_path, 'EmpiricalModel')

    def predict(self, tokens):
        if self.prob_table:
            return self.prob_table[tokens]

    def train(self):
        if self.is_valid_corpus():
            self.prob_table = Counter()
            for s in open(self.corpus_path, 'r'):
                token = [s.split('\n')[0]]
                self.prob_table.update(token)
            total = 1.0 * sum(self.prob_table.values())
            for k in self.prob_table:
                self.prob_table[k] /= total
