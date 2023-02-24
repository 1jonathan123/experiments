class Creator:
    def __init__(self, spaces_number):
        self._spaces_number = spaces_number

    def _add_spaces(self, word):
        return (' ' * self._spaces_number).join(word)

    def __call__(self, data):
        return f"{data[0][0].upper() + data[0][1:]}\nCan the letter sequence \"{self._add_spaces(data[1])}\" form a word in English?\nA:"
