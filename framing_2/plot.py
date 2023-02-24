from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s_from_ln
import matplotlib.pyplot as plt
from functools import partial

import numpy as np


def da_to_xy(options, swap_chance, data, answer):
    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    chance = data[-1]
    if swap_chance:
        chance = 100 - chance

    return chance, true_prob


def plot():
    counter = 0

    for description, to_swap in zip(['success', 'failure'], [False, True]):
        for compare, options in zip(['better', 'worse'], [['yes', 'no'], ['no', 'yes']]):
            label = description + '_' + compare
            graph = [get_xa('results/' + label, partial(da_to_xy, options, to_swap))]

            if compare == 'better':
                plt.plot(*get_average_xy_s_from_ln(graph), label='describing ' + description)

            counter += 1

    # graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in range(len(labels))]
    # plt.plot(*get_average_xy_s_from_ln(graph), label="average")

    plt.ylabel('Better than average')
    plt.xlabel('Success chances')

    plt.legend()
    plt.show()


def main():
    plot()


if __name__ == "__main__":
    main()
