from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error, \
    IgnoreThisException, get_average_xy_s_from_ln
import matplotlib.pyplot as plt
from functools import partial

import numpy as np

from constants import animals


def da_to_xy_distance(options, data, answer):
    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return abs(animals.index(data[1]) - animals.index(data[2])), true_prob


def da_to_xy_size(options, delta, data, answer):
    if abs(animals.index(data[1]) - animals.index(data[2])) != delta:
        raise IgnoreThisException

    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return len(animals) - max(animals.index(data[1]), animals.index(data[2])), true_prob


def da_to_xy_semantic(options, data, answer):
    if max(animals.index(data[1]), animals.index(data[2])) < len(animals) / 2:
        both_large = True
    elif min(animals.index(data[1]), animals.index(data[2])) > len(animals) / 2:
        both_large = False
    else:
        raise IgnoreThisException

    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return 1 if both_large else 0, true_prob


def da_to_xy_snarc(options, data, answer):
    prob = [np.logaddexp.reduce([answer[k] for k in answer if k.lower().strip() in o]) for o in options]

    true_prob = prob[0] - np.logaddexp.reduce(prob)

    return 0, true_prob


def get_to_xy(f, *argv):
    return [
        partial(f, ['no', 'yes'], *argv),
        partial(f, ['yes', 'no'], *argv),
        partial(f, ['yes', 'no'], *argv),
        partial(f, ['no', 'yes'], *argv),
    ]


labels = [
    'no_bigger',
    'yes_bigger',
    'yes_smaller',
    'no_smaller',
]


def plot_distance():
    to_xy = get_to_xy(da_to_xy_distance)

    for i in range(0, 0):
        graph = [get_xa(f'results/' + labels[i], to_xy[i])]

        plt.plot(*get_average_xy_s_from_ln(graph), label=labels[i])

    graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in range(4)]
    plt.plot(*get_average_xy_s_from_ln(graph), label="average")

    plt.ylabel('Assurance')
    plt.xlabel('Distance')

    plt.legend()
    plt.show()


def plot_size(s=1):
    to_xy = get_to_xy(da_to_xy_size, s)

    for i in range(0, 0):
        graph = [get_xa(f'results/' + labels[i], to_xy[i])]

        plt.plot(*get_average_xy_s_from_ln(graph), label=labels[i])

    graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in range(4)]
    plt.plot(*get_average_xy_s_from_ln(graph), label="average")

    plt.ylabel('Assurance')
    plt.xlabel('Base')

    plt.legend()
    plt.show()


def plot_semantic():
    to_xy = get_to_xy(da_to_xy_semantic)

    for i in range(0, 0):
        graph = [get_xa(f'results/' + labels[i], to_xy[i])]

        plt.plot(*get_average_xy_s_from_ln(graph), label=labels[i])

    graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in range(0, 2)]
    plt.plot(*get_average_xy_s_from_ln(graph), label="bigger")

    graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in range(2, 4)]
    plt.plot(*get_average_xy_s_from_ln(graph), label="smaller")

    plt.ylabel('Assurance')
    plt.xlabel('Distance')

    plt.legend()
    plt.show()


def plot_snarc():
    to_xy = get_to_xy(da_to_xy_snarc)

    graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in [0, 2]]
    plt.plot(*get_average_xy_s_from_ln(graph))
    print(*get_average_xy_s_from_ln(graph))

    graph = [get_xa(f'results/' + labels[i], to_xy[i]) for i in [1, 3]]
    plt.plot(*get_average_xy_s_from_ln(graph))
    print(*get_average_xy_s_from_ln(graph))

    plt.ylabel('Assurance')
    plt.xlabel('Distance')

    #plt.legend()
    #plt.show()


def main():
    plot_distance()


if __name__ == "__main__":
    main()
