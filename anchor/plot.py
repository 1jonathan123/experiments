from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException
import matplotlib.pyplot as plt
import os, sys
from functools import partial


def da_to_xy(data, answer):
    return data[-1], int(get_greedy_answer(answer))


def get_xy(directories, directory, func=da_to_xy, label=None):
    if label is None:
        label = directory

    xa = {}

    for d in directories:
        xa = get_xa(os.path.join(d, directory), func, xa)

    print(f'{label}: {get_average_distance(xa)} {get_average_error(xa)}')

    return get_average_xy(xa)


def plot_average():
    plt.plot(list(range(30, 70)), list(range(30, 70)), color='green', label='true value')

    plt.plot(*get_xy(sys.argv[1:], 'small'), color='red', label='small examples.txt')
    plt.plot(*get_xy(sys.argv[1:], 'balanced'), color='purple', label='balanced examples.txt')
    plt.plot(*get_xy(sys.argv[1:], 'large'), color='blue', label='large examples.txt')

    plt.xlabel('objects to count')
    plt.ylabel('estimation')

    plt.legend()
    plt.show()


def da_to_xy_large(index, data, answer):
    if data[index] <= 70:
        raise IgnoreThisException

    return data[-1], int(get_greedy_answer(answer))


def da_to_xy_small(index, data, answer):
    if data[index] >= 30:
        raise IgnoreThisException

    return data[-1], int(get_greedy_answer(answer))


def plot_with_respect_to_last():

    for i in range(4):
        get_xy(sys.argv[1:], 'balanced', partial(da_to_xy_large, i), f'{i} large')
        get_xy(sys.argv[1:], 'balanced', partial(da_to_xy_small, i), f'{i} small')

    get_xy(sys.argv[1:], 'balanced')


def main():
    plot_average()
    #plot_with_respect_to_last()


if __name__ == "__main__":
    main()
