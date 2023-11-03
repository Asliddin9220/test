class Trip:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __str__(self):
        return f"{self._start}, {self._end}"