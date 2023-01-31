from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s_from_ln
import matplotlib.pyplot as plt
from functools import partial

import numpy as np


def da_to_xy(options, index, data, answer):
    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return data[index], true_prob


def plot_average():
    to_xy = [
        partial(da_to_xy, ['a', 'b'], -1),
        partial(da_to_xy, ['b', 'a'], 2),
        partial(da_to_xy, ['1', '2'], -1),
        partial(da_to_xy, ['2', '1'], 2),
    ]

    labels = [
        'A is the safe',
        'B is the safe',
        '1 is the safe',
        '2 is the safe',
    ]

    for i in range(0, 1):
        graph = [get_xa(f'results/' + str(i), to_xy[i])]

        plt.plot(*get_average_xy_s_from_ln(graph), label=labels[i])

    #graph = [get_xa(f'results/' + str(i), to_xy[i]) for i in range(0, 2)]
    #plt.plot(*get_average_xy_s_from_ln(graph))

    plt.ylabel('Choosing the safe 60, instead of 80% to')
    plt.xlabel('alternative')

    plt.legend()
    plt.show()


def main():
    plot_average()


if __name__ == "__main__":
    main()
