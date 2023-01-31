from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s_from_ln
import matplotlib.pyplot as plt
from functools import partial

import numpy as np


def da_to_xy(parity, data, answer):
    if data[-1] % 2 != parity:
        raise IgnoreThisException

    odd = ['odd', '1', 'one']
    even = ['even', '0', 'zero']

    odd_prob = np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in odd])
    even_prob = np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in even])

    prob = [even_prob, odd_prob]

    true_prob = prob[parity] - np.logaddexp.reduce(prob)

    return data[-1], true_prob


def xas_to_xa(left, right):
    xa = {}

    for l, r in zip(left, right):
        for k in l:
            if not k in xa:
                xa[k] = []
            xa[k] += [l_ - r_ for l_, r_ in zip(l[k], r[k])]

    return xa


def plot_average():
    r = range(4, 7)
    to_prob = False
    left_even = [get_xa(f'left{i}', partial(da_to_xy, 0), to_prob) for i in r]
    left_odd = [get_xa(f'left{i}', partial(da_to_xy, 1), to_prob) for i in r]
    right_even = [get_xa(f'right{i}', partial(da_to_xy, 0), to_prob) for i in r]
    right_odd = [get_xa(f'right{i}', partial(da_to_xy, 1), to_prob) for i in r]
    neutral_even = [get_xa(f'neutral{i}', partial(da_to_xy, 0), to_prob) for i in r]
    neutral_odd = [get_xa(f'neutral{i}', partial(da_to_xy, 1), to_prob) for i in r]

    # plt.plot(*get_average_xy(xas_to_xa(left_odd, right_odd)), label=f'odd')
    # plt.plot(*get_average_xy(xas_to_xa(left_even, right_even)), label=f'even')
    # plt.plot(*get_average_xy(xas_to_xa(neutral_odd, right_odd)), label=f'odd neutral vs right')
    # plt.plot(*get_average_xy(xas_to_xa(neutral_even, right_even)), label=f'even neutral vs right')
    # plt.plot(*get_average_xy(xas_to_xa(neutral_even, right_even)), label=f'even')

    plt.plot(*get_average_xy_s_from_ln(left_even), label=f'left, even')
    #plt.plot(*get_average_xy_s_from_ln(left_odd), label=f'left, odd')

    plt.plot(*get_average_xy_s_from_ln(right_even), label=f'right, even')
    #plt.plot(*get_average_xy_s_from_ln(right_odd), label=f'right, odd')

    # plt.plot(*get_average_xy_s_from_ln(neutral_even), label=f'neutral, even')
    #plt.plot(*get_average_xy_s_from_ln(neutral_odd), label=f'neutral, odd')

    plt.legend()
    plt.show()


def main():
    plot_average()


if __name__ == "__main__":
    main()
