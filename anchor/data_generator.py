from random import randint, shuffle


class DataGenerator:

    def __init__(self, examples_range, question_range, repeat=1, shuffle_examples=True):
        self._repeat = repeat
        self._examples_range = examples_range
        self._shuffle_examples = shuffle_examples
        self._question_range = (*question_range[:1], question_range[1] + 1, *question_range[2:])

    def __iter__(self):
        for _ in range(self._repeat):
            for i in range(*self._question_range):
                data = []
                for r in self._examples_range:
                    data.append(randint(*r))

                if self._shuffle_examples:
                    shuffle(data)

                yield data + [i]
