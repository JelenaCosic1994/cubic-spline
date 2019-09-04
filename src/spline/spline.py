from src.spline.cubic import CubicPolynomial


class Spline:

    def __init__(self):
        self._ranges = []
        self._cubic_polynomials = []

    def add_cubic_polynomial_for_range(self, cubic_polynomial, x1, x2):
        self._ranges.append((x1, x2))
        self._cubic_polynomials.append(cubic_polynomial)

    def get_ranges_and_functions(self):
        return [{'range': self._ranges[i], 'function': self._cubic_polynomials[i].get_function()}
                for i in range(len(self._ranges))]
