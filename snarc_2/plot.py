from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s_from_ln

import numpy as np

import sys

options = [[str(i) for i in range(1, 4 + 1)], [str(i) for i in range(6, 9 + 1)]]


def da_to_xy(data, answer):
    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return 0, true_prob


def plot():
    graph = get_xa("results/" + sys.argv[1], da_to_xy)
    print(*get_average_xy_s_from_ln([graph]))


def main():
    plot()


if __name__ == "__main__":
    main()
