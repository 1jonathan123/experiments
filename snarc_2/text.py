class Creator:
    def __init__(self, text, priming):
        self._text = text
        self._priming = priming

    def __call__(self, data):
        result = ''
        for d in data:
            result += self._priming[d]

        return ' '.join([self._priming[d] for d in data]) + '\n' + self._text
