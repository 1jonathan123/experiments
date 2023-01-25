from random import choice


class DataGenerator:

    def __init__(self, words_number, possible_words, numbers_range, repeat=1):
        self._words_number = words_number
        self._possible_words = possible_words
        self._numbers_range = (*numbers_range[:1], numbers_range[1] + 1, *numbers_range[2:])
        self._repeat = repeat

    def __iter__(self):
        for _ in range(self._repeat):  # TODO: another generator for repeat
            for i in range(*self._numbers_range):
                data = []
                for _ in range(self._words_number):
                    data.append(choice(self._possible_words))

                yield data + [i]
