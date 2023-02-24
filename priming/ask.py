from llm_evaluator.run import just_print, ask_permissions, run
from llm_evaluator.text import NoiseCreator, NoiseData
from llm_evaluator.predict import gpt3_one_token

from text import Creator as TextCreator
from constants import *


def main():
    ask_permissions()

    text = NoiseCreator(TextCreator(3), '_')

    data = []

    for primer in unrelated_words + related_words:
        for stimulus in not_words: #related_words:
            if primer != stimulus:
                data.append((primer, stimulus))

    run(text, NoiseData(data, range(30, 61)), gpt3_one_token, 'results/3_not_words')


if __name__ == "__main__":
    main()
