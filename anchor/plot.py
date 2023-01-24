from llm_evaluator.plot import get_xa, get_average_xy, get_greedy_answer, get_average_distance, get_average_error
import matplotlib.pyplot as plt
import os, sys


def da_to_xy(data, answer):
    return data[-1], int(get_greedy_answer(answer))


def get_xy(directories, directory):
    xa = {}

    for d in directories:
        xa = get_xa(os.path.join(d, directory), da_to_xy, xa)

    distance = 0
    denominator = 0

    for x in xa:
        denominator += len(xa[x])
        for y in xa[x]:
            distance += y - x

    print(f'{directory}: {get_average_distance(xa)} {get_average_error(xa)}')

    return get_average_xy(xa)


def main():
    plt.plot(list(range(30, 70)), list(range(30, 70)), color='green', label='true value')

    plt.plot(*get_xy(sys.argv[1:], 'small'), color='red', label='small examples')
    plt.plot(*get_xy(sys.argv[1:], 'balanced'), color='purple', label='balanced examples')
    plt.plot(*get_xy(sys.argv[1:], 'large'), color='blue', label='large examples')

    plt.xlabel('objects to count')
    plt.ylabel('estimation')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
