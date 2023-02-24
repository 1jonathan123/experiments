from llm_evaluator.run import just_print, ask_permissions, run
from llm_evaluator.text import NoiseCreator, NoiseData
from llm_evaluator.predict import gpt3_one_token

from data import Generator as DataGenerator
from text import Creator as TextCreator

from constants import animals


def main():
    ask_permissions()

    bigger_to_smaller_data = NoiseData(DataGenerator(animals), range(20, 70))
    bigger_text = NoiseCreator(TextCreator('bigger'), '_')

    smaller_to_bigger_data = NoiseData(DataGenerator(list(reversed(animals))), range(20, 70))
    smaller_text = NoiseCreator(TextCreator('smaller'), '_')

    run(bigger_text, bigger_to_smaller_data, gpt3_one_token, 'results/yes_bigger')
    run(bigger_text, smaller_to_bigger_data, gpt3_one_token, 'results/no_bigger')
    run(smaller_text, bigger_to_smaller_data, gpt3_one_token, 'results/no_smaller')
    run(smaller_text, smaller_to_bigger_data, gpt3_one_token, 'results/yes_smaller')


if __name__ == "__main__":
    main()
