from EmpiricalDistribution import EmpiricalDistribution


def run_empirical():
    e = EmpiricalDistribution('./corpora/clean/brown_clean.txt')
    e.train()
    for k in e.prob_table:
        print(k, e.prob_table[k])
        break

if __name__ == '__main__':
    run_empirical()