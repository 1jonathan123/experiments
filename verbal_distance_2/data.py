class Generator:
    def __init__(self, comparable_objects):
        self._comparable_objects = comparable_objects

    def __iter__(self):
        for i in range(len(self._comparable_objects)):
            for j in range(i + 1, len(self._comparable_objects)):
                yield self._comparable_objects[i], self._comparable_objects[j]
