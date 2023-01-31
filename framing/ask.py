from llm_evaluator.run import just_print, run, ask_permissions
from llm_evaluator.predict import gpt3_one_token

from text import create_text

import itertools


def main():
    if not ask_permissions():
        return

    texts = \
        [create_text('_', 'There are two options:', ['A)', 'B)'], 0, 'The better option is option'),

         create_text('-', 'Out of the next two options:', ['1)', '2)'], 1,
                     'The option with the higher utility is option'),

         create_text('_', 'There are two options:', ['A)', 'B)'], 2, 'The better option is option'),

         create_text('-', 'Out of the next two options:', ['1)', '2)'], 3,
                     'The option with the higher utility is option'),
         ]

    datas = \
        [list(itertools.product(range(20, 71), range(100, 101), range(60, 61), range(80, 81), range(65, 101))),
         list(itertools.product(range(20, 71), range(80, 81), range(65, 101), range(100, 101), range(60, 61)))]

    for i, (text, data) in enumerate(itertools.product(texts, datas)):
        run(text, data, gpt3_one_token, "results/" + str(i))


if __name__ == "__main__":
    main()
