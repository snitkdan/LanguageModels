from EmpiricalDistribution import EmpiricalDistribution
from Unigram import Unigram
import pdb

brown_clean = './corpora/clean/brown_clean.txt'

def head(n, prob_table):
    c = 0
    for i in prob_table:
        print(i, prob_table[i])
        c += 1
        if c == n:
            break


def run(Model, corpus, preview_len):
    m = Model(corpus)
    m.train()
    head(preview_len, m.prob_table)


def run_empirical():
    run(EmpiricalDistribution, brown_clean, 1)


def run_unigram():
    run(Unigram, brown_clean, 10)


if __name__ == '__main__':
    run_empirical()
    print('\n')
    run_unigram()