class LanguageModel(object):

    def __init__(self, corpus_path=None, model_name='LanguageModel'):
        self.corpus_path = corpus_path
        self.model_name = model_name

    def __str__(self):
        return '{1} with {0} corpus'.format(self.corpus_path, self.model_name)

    def normalize(self, total, prob_table):
        for k in prob_table:
            prob_table[k] /= total

    def get_corpus_path(self):
        return self.corpus_path

    def set_corpus_path(self, corpus_path):
        self.corpus_path = corpus_path

    def is_valid_corpus(self):
        try:
            open(self.corpus_path, 'r')
        except FileNotFoundError:
            return False
        return True

