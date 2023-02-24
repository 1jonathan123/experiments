from llm_evaluator.run import just_print, ask_permissions, run
from llm_evaluator.predict import gpt3_one_token

from text import Creator as TextCreator


def main():
    ask_permissions()

    wordings = [
        #'A random digit:',
        #'Random digit:',
        'A random single digit number:\n\n',
        'Random single digit number:\n\n'
    ]

    primers = [
        # ['apple', 'Apple'],
        # [' apple', ' Apple']
        # ['left', 'Left'],
        # ['right', 'Right']
        # ['center', 'Center'],
        # ['middle', 'Middle']
        #['smith', 'Smith'],
        #['lee', 'Lee']
        ['up', 'Up'],
        ['down', 'Down']
    ]

    data = [[int(b) for b in '0' * (9 - len(bin(i)[2:])) + bin(i)[2:]] for i in range(512)]

    for i, wording in enumerate(wordings):
        for primer in primers:
            run(TextCreator(wording, primer), data, gpt3_one_token, "results/" + primer[0] + '_' + str(i + 2))


if __name__ == "__main__":
    main()
