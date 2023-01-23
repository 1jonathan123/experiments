from llm_evaluator.text import Sequence, List, Constant, Final


class TextCreator:

    def __init__(self, characters, examples_number, question_prefix,
                 question_suffix, question_answer_separator, answers_suffix='\n'):
        self._characters = characters
        self._examples_number = examples_number
        self._question_prefix = question_prefix
        self._question_suffix = question_suffix
        self._question_answer_separator = question_answer_separator
        self._answers_suffix = answers_suffix
        self._data_generators = []

    def create_question(self, length_generator):
        return List([
            Constant(self._question_prefix),
            Sequence(Constant(self._characters), length_generator),
            Constant(self._question_suffix)
        ])

    def create_answer(self, length_generator):
        return List([Constant(self._question_answer_separator), length_generator, Constant(self._answers_suffix)])

    def create_length(self):
        self._data_generators.append(Constant())
        return self._data_generators[-1]

    def create_example(self):
        length = self.create_length()
        return List([self.create_question(length), self.create_answer(length)])

    def create_output(self):
        return List([self.create_example() for _ in range(self._examples_number)] +
                    [self.create_question(self.create_length())])

    def __call__(self):
        return Final(self.create_output(), self._data_generators, self._data_generators)


def create_text(*argv, **kwargs):
    return TextCreator(*argv, **kwargs)()
