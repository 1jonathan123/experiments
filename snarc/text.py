from llm_evaluator.text import Sequence, List, Constant, Final


class TextCreator:

    def __init__(self, words_number, prefix, suffix):
        self._words_number = words_number
        self._prefix = Constant(prefix)
        self._suffix = Constant(suffix)
        self._data_generators = []

    def _create_question(self):
        self._data_generators.append(Constant())
        return List([self._prefix, self._data_generators[-1], self._suffix])

    def _create_word(self, suffix):
        self._data_generators.append(Constant())
        return List([self._data_generators[-1], Constant(suffix)])

    def _create_words(self):
        if self._words_number == 0:
            return []

        return List([self._create_word(' ') for _ in range(self._words_number - 1)] + [self._create_word('\n')])

    def _create_output(self):
        return List([self._create_words(), self._create_question()])

    def __call__(self):
        return Final(self._create_output(), self._data_generators, self._data_generators)


def create_text(*argv, **kwargs):
    return TextCreator(*argv, **kwargs)()
