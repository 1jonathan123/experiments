class Creator:

    def __init__(self, description, compare_word):
        self._description = description
        self._compare_word = compare_word

    def __call__(self, data):
        return f'''Every surgery ends with either success or failure.
Q: Is {data[0]}% {self._description} chance for cardiac surgery {self._compare_word} than the general average? (yes/no only)
A:'''
