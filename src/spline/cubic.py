from numpy import poly1d


class CubicPolynomial:

    def __init__(self, a0, a1, a2, a3):
        """a0*x^3 + a1*x^2 + a2*x + a3"""
        self._a0 = a0
        self._a1 = a1
        self._a2 = a2

    def get_function(self):
        return poly1d([self._a0, self._a1, self._a2, self._a3])
