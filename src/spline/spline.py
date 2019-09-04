class Spline:

    def __init__(self):
        self._ranges = []
        self._functions = []

    def add_function_for_range(self, function, x1, x2):
        self._ranges.append((x1, x2))
        self._functions.append(function)

