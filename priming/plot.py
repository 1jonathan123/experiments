from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s_from_ln

import numpy as np

from constants import *

options = ['yes', 'no']


def da_to_xy(data, answer):
    #if data[2] != 'hospital':
        #raise IgnoreThisException

    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() == o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return 1 if data[1] in related_words else 0, true_prob


def plot():
    graph = get_xa(f'results/20', da_to_xy)
    print(*get_average_xy_s_from_ln([graph]))


def main():
    plot()


if __name__ == "__main__":
    main()
