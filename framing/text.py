from llm_evaluator.text import Sequence, List, Constant, Final


class TextCreator:

    def __init__(self, noise, prefix, options, option_type, suffix):
        self._noise = Constant(noise)
        self._prefix = Constant(prefix)
        self._options = [Constant(option) for option in options]
        self._option_type = option_type
        self._suffix = Constant(suffix)
        self._data_generators = []

    def _create_noise(self):
        self._data_generators.append(Constant())

        return Sequence(self._noise, self._data_generators[-1])

    def _create_option(self, number):
        for i in range(2):
            self._data_generators.append(Constant())

        if self._option_type == 0:
            return List([self._options[number], Constant(' '), self._data_generators[-2], Constant('% chance to earn '),
                         self._data_generators[-1], Constant(' euros.')])

        if self._option_type == 1:
            return List([self._options[number], Constant(' Earning '), self._data_generators[-1],
                         Constant(' euros with '),
                         self._data_generators[-2], Constant('% chance.')])

        if self._option_type == 2:
            return List([self._options[number], Constant(' '), self._data_generators[-2], Constant('% chance to lose '),
                         self._data_generators[-1], Constant(' euros.')])

        if self._option_type == 3:
            return List([self._options[number], Constant(' Losing '), self._data_generators[-1],
                         Constant(' euros with '),
                         self._data_generators[-2], Constant('% chance.')])

        raise Exception("Unknown option")

    def _create_output(self):
        return List(
            [self._create_noise(), Constant('\n'), self._prefix, Constant('\n'), self._create_option(0), Constant('\n'),
             self._create_option(1), Constant('\n'), self._suffix])

    def __call__(self):
        return Final(self._create_output(), self._data_generators, self._data_generators)


def create_text(*argv, **kwargs):
    return TextCreator(*argv, **kwargs)()
