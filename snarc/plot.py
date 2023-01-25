from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s
import matplotlib.pyplot as plt
import os, sys
from functools import partial


def da_to_xy(parity, data, answer):
    if data[-1] % 2 != parity:
        raise IgnoreThisException

    odd = ['odd', '1', 'one']
    even = ['even', '0', 'zero']

    odd_prob = sum(answer[k] for k in answer if k.lower().strip() in odd)
    even_prob = sum(answer[k] for k in answer if k.lower().strip() in even)

    prob = [even_prob, odd_prob]

    true_prob = prob[parity] / sum(prob)

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
    left_even = [get_xa(f'left{i}', partial(da_to_xy, 0)) for i in r]
    left_odd = [get_xa(f'left{i}', partial(da_to_xy, 1)) for i in r]
    right_even = [get_xa(f'right{i}', partial(da_to_xy, 0)) for i in r]
    right_odd = [get_xa(f'right{i}', partial(da_to_xy, 1)) for i in r]
    neutral_even = [get_xa(f'neutral{i}', partial(da_to_xy, 0)) for i in r]
    neutral_odd = [get_xa(f'neutral{i}', partial(da_to_xy, 1)) for i in r]

    #plt.plot(*get_average_xy(xas_to_xa(left_odd, right_odd)), label=f'odd')
    #plt.plot(*get_average_xy(xas_to_xa(left_even, right_even)), label=f'even')
    #plt.plot(*get_average_xy(xas_to_xa(neutral_odd, right_odd)), label=f'odd neutral vs right')
    #plt.plot(*get_average_xy(xas_to_xa(neutral_even, right_even)), label=f'even neutral vs right')
    #plt.plot(*get_average_xy(xas_to_xa(neutral_even, right_even)), label=f'even')

    plt.plot(*get_average_xy_s(left_even), label=f'left, even')
    plt.plot(*get_average_xy_s(left_odd), label=f'left, odd')

    #plt.plot(*get_average_xy_s(right_even), label=f'right, even')
    #plt.plot(*get_average_xy_s(right_odd), label=f'right, odd')

    # plt.plot(*get_average_xy(get_xa('left', partial(da_to_xy, 0))), color='red', label='left, even')
    # plt.plot(*get_average_xy(get_xa('left', partial(da_to_xy, 1))), color='blue', label='left, odd')
    # plt.plot(*get_average_xy(get_xa('right', partial(da_to_xy, 0))), color='yellow', label='right1, even')
    # plt.plot(*get_average_xy(get_xa('right', partial(da_to_xy, 1))), color='green', label='right, odd')
    # plt.plot(*get_average_xy(get_xa('neutral', partial(da_to_xy, 0))), color='purple', label='neutral, even')
    # plt.plot(*get_average_xy(get_xa('neutral', partial(da_to_xy, 1))), color='orange', label='neutral, odd')

    # plt.plot(*get_average_xy(get_xa('left_', partial(da_to_xy, 0))), color='black', label='left_, even')
    # plt.plot(*get_average_xy(get_xa('left_', partial(da_to_xy, 1))), color='pink', label='left_, odd')
    # plt.plot(*get_average_xy(get_xa('right_', partial(da_to_xy, 0))), color='gray', label='right_, even')
    # plt.plot(*get_average_xy(get_xa('right_', partial(da_to_xy, 1))), color='brown', label='right_, odd')
    # plt.plot(*get_average_xy(get_xa('neutral_', partial(da_to_xy, 0))), color='darkgreen', label='neutral_, even')
    # plt.plot(*get_average_xy(get_xa('neutral', partial(da_to_xy, 1))), color='darkorange', label='neutral, odd')

    # plt.xlabel('objects to count')
    # plt.ylabel('estimation')

    plt.legend()
    plt.show()


def main():
    plot_average()


if __name__ == "__main__":
    main()
