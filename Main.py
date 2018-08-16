from EmpiricalDistribution import EmpiricalDistribution
from Unigram import Unigram
from Bigram import Bigram

brown_clean = './corpora/clean/brown_clean.txt'


def head(n, prob_table):
    c = 0
    for i in prob_table:
        print(i, prob_table[i])
        c += 1
        if c == n:
            break


def run(model, corpus, preview_len):
    m = model(corpus)
    m.train()
    head(preview_len, m.prob_table)
    print()


def run_empirical():
    run(EmpiricalDistribution, brown_clean, 10)

def run_unigram():
    run(Unigram, brown_clean, 10)

def run_bigram():
    run(Bigram, brown_clean, 10)


if __name__ == '__main__':
    run_empirical()
    run_unigram()
    run_bigram()