def add_a(word):
    if word[0] in 'aeiou':
        return 'an ' + word
    return 'a ' + word


class Creator:

    def __init__(self, compare_word):
        self._compare_word = compare_word

    def __call__(self, data):
        return f'Q: Is {add_a(data[0])} {self._compare_word} than {add_a(data[1])}?\nA:'
