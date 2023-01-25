from text import create_text
from data import DataGenerator
from llm_evaluator.run import just_print, run, ask_permissions
from llm_evaluator.predict import gpt3_one_token


def left_data():
    return DataGenerator(10, ['Left', '<-', 'left', '<--'], (1, 9), 50)


def right_data():
    return DataGenerator(10, ['Right', '->', 'right', '-->'], (1, 9), 50)


def neutral_data():
    return DataGenerator(10, ['Center', '-', 'center', '--'], (1, 9), 50)


def left_data_minimalistic():
    return DataGenerator(10, ['Left', 'left'], (1, 9), 50)


def right_data_minimalistic():
    return DataGenerator(10, ['Right', 'right'], (1, 9), 50)


def neutral_data_minimalistic():
    return DataGenerator(10, ['Center', 'center'], (1, 9), 50)


def main():
    text1 = create_text(10, 'The parity of ', ' is')
    text2 = create_text(10, 'The parity of the number ', ' is')
    text3 = create_text(10, "", "'s parity is")
    left = left_data_minimalistic()
    right = right_data_minimalistic()
    neutral = neutral_data_minimalistic()

    if not ask_permissions():
        return

    run(text1, left, gpt3_one_token, 'left4')
    run(text2, left, gpt3_one_token, 'left5')
    run(text3, left, gpt3_one_token, 'left6')

    run(text1, right, gpt3_one_token, 'right4')
    run(text2, right, gpt3_one_token, 'right5')
    run(text3, right, gpt3_one_token, 'right6')

    run(text1, neutral, gpt3_one_token, 'neutral4')
    run(text2, neutral, gpt3_one_token, 'neutral5')
    run(text3, neutral, gpt3_one_token, 'neutral6')


if __name__ == "__main__":
    main()
