from data_generator import DataGenerator
from create_text import create_text
from llm_evaluator.run import run
from llm_evaluator.predict import gpt3_one_token


def main():
    text = create_text('!@', 4, "len('", "') # equals to", ' ')
    small_data = DataGenerator([(10, 29)] * 4, (30, 70), 10)
    run(text, small_data, gpt3_one_token, 'small')

    balanced_data = DataGenerator([(10, 29)] * 2 + [(71, 90)] * 2, (30, 70), 10)
    run(text, balanced_data, gpt3_one_token, 'balanced')

    large_data = DataGenerator([(71, 90)] * 4, (30, 70), 10)
    run(text, large_data, gpt3_one_token, 'large')


if __name__ == "__main__":
    main()
