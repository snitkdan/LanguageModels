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

def run_empirical():
    e = EmpiricalDistribution(brown_clean)
    e.train()
    head(5, e.prob_table)

def run_unigram():
    u = Unigram(brown_clean)
    u.train()
    head(10, u.prob_table)


if __name__ == '__main__':
    run_empirical()
    print('\n')
    run_unigram()