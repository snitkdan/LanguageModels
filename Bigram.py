from Ngram import Ngram
from random import choice
from collections import Counter

class Bigram(Ngram):

    def __init__(self, corpus_path=None):
        super(Bigram, self).__init__(corpus_path, 'BigramModel')

    def get_token_gen(self, tokens):
        yield('START', tokens[0])
        for i in range(len(tokens) - 1):
            yield (tokens[i], tokens[i+1])
        yield(tokens[len(tokens) - 1], 'STOP')

    def get_filtered_cnter(self, el, cnter):
        return Counter({k: cnter[k] for k in cnter if k[0] == el})

    def get_start_cnter(self):
        return self.get_filtered_cnter('START', self.count_table)

    def sample(self, cnter):
        return choice(list(cnter.elements()))

    def cnter_diff(self, subtractee, subtracter):
        return Counter({k: subtractee[k] for k in subtractee if k not in subtracter})

    def generate_sentence(self):
        if self.count_table:
            sentence = []
            start_cnter = self.get_start_cnter()
            next_token = self.sample(start_cnter)
            rest = self.cnter_diff(self.count_table, start_cnter)
            while next_token[1] != 'STOP':
                sentence.append(next_token[1])
                next_token = self.sample(self.get_filtered_cnter(next_token[1], rest))
            return ' '.join(sentence)
        return ''


