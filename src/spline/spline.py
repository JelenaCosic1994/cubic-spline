from src.spline.cubic import CubicPolynomial


class Spline:

    def __init__(self):
        self._ranges = []
        self._cubic_polynomials = []

    def add_cubic_polynomial_for_range(self, coefficients, x1, x2):
        """
        This method adds cubic polynomial specified via coefficients (a0, a1, a2, a3) to specific range
        :param coefficients: array([a0, a1, a2, a3]) used for cubic polynomial creation
        :param x1: range lower bound
        :param x2: range upper bound
        """
        self._ranges.append((x1, x2))
        self._cubic_polynomials.append(CubicPolynomial(*coefficients))

    def get_ranges_and_functions(self):
        """
        :return: List of pairs(dictionaries): range, function. Range is specified as tuple
        e.g. (lower_bound, upper_bound)
        """
        return [{'range': self._ranges[i], 'function': self._cubic_polynomials[i].get_function()}
                for i in range(len(self._ranges))]
