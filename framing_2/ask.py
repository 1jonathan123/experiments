from llm_evaluator.run import just_print, ask_permissions, run
from llm_evaluator.text import NoiseCreator, NoiseData
from llm_evaluator.predict import gpt3_one_token

from text import Creator as TextCreator


def main():
    ask_permissions()

    for description in ['success', 'failure']:
        for compare in ['better', 'worse']:
            text = NoiseCreator(TextCreator(description, compare), '_')

            run(text, NoiseData(((i,) for i in range(1, 100)), range(30, 61)), gpt3_one_token,
                'results/' + description + '_' + compare)


if __name__ == "__main__":
    main()
