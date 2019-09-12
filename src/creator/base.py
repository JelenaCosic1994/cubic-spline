import numpy as np
import math
from src.spline.spline import Spline
from abc import ABC, abstractmethod


class BaseSplineCreator(ABC):

    @abstractmethod
    def get_m(self, **kwargs):
        pass

    @staticmethod
    def calculate_raw_spline(alpha, beta, gamma, delta, x, n):
        """
        Calculate spline
        """
        raw_spline = []
        for i in range(0, n):
            s1 = np.hstack((np.zeros(n+1), np.array(alpha[i])))
            s2 = np.hstack((np.zeros(n), np.array((beta[i], -beta[i] * x[i]))))
            s3 = np.hstack((np.zeros(n - 1), np.array((gamma[i], -2 * gamma[i] * x[i], gamma[i] * x[i] ** 2))))
            s4 = np.hstack((np.zeros(n - 2), np.array((delta[i], -3 * delta[i] * x[i], 3 * delta[i] * x[i] ** 2,
                                                       -delta[i] * math.pow(x[i], 3)))))

            raw_spline.append(s1 + s2 + s3 + s4)
        return raw_spline

    @staticmethod
    def convert_raw_spline_into_spline(raw_spline, x, n):
        spline = Spline()
        for i in range(0, n):
            x1 = x[i]
            x2 = x[i+1]
            spline_coefficients = raw_spline[i][-4:]
            spline.add_cubic_polynomial_for_range(spline_coefficients, x1, x2)
        return spline

    @staticmethod
    def calculate_coefficients(h, f, M, n):
        """
        Calculate coefficients alpha, beta, gamma and delta
        :param h: distances between points
        :param f: function values
        :param M: moments
        :param n: length
        :return: coefficients alpha, beta, gamma and delta
        """
        alpha = []
        beta = []
        gamma = []
        delta = []
        for i in range(0, n):  # from 0 to n-1 (n elements)
            alpha.append(f[i])
            beta.append((f[i + 1] - f[i]) / h[i+1] - h[i+1] / 6 * (2 * M[i] + M[i + 1]))
            gamma.append(1 / 2 * M[i])
            delta.append((1 / (6 * h[i+1])) * (M[i + 1] - M[i]))

        return alpha, beta, gamma, delta

    @staticmethod
    def calculate_ni_mi_lambda(f, h, n):
        """
        Calculate coefficients mi, ni and lambda
        :param f: function values
        :param h: distances between points
        :param n: length
        :return: coefficients mi, ni and lambda
        """
        ni = [None] * n  # (length = n) zero element added for easier indexing
        mi = [None] * n  # (length = n) zero element added for easier indexing
        lambd = [None] * n  # (length = n) zero element added for easier indexing

        for i in range(1, n):  # 1, 2,.. n-1
            ni[i] = h[i+1] / (h[i] + h[i+1])
            mi[i] = 1 - ni[i]
            lambd[i] = (6/(h[i] + h[i+1]))*((f[i+1] - f[i])/h[i+1] - (f[i] - f[i-1])/h[i])

        mi = mi[1:]
        ni = ni[1:]
        lambd = lambd[1:]

        return ni, mi, lambd

    def cubic_spline(self, t, **kwargs):

        x = t[0, :]  # (length = n + 1) x0, x1, x2,.. xn
        f = t[1, :]  # (length = n + 1) x0, x1, x2,.. xn
        h = [None] + list(np.diff(x))  # distances between points (length = n + 1), zero element is not in use,
        # zero element added for easier indexing

        n = len(x) - 1  # x0, x1,.. xn (n is n from index of x_n)

        ni, mi, lambd = BaseSplineCreator.calculate_ni_mi_lambda(f, h, n)

        M = self.get_m(n=n, h=h, f=f, ni=ni, mi=mi, lambd=lambd, **kwargs)

        alpha, beta, gamma, delta = BaseSplineCreator.calculate_coefficients(h, f, M, n)

        return BaseSplineCreator.convert_raw_spline_into_spline(
            BaseSplineCreator.calculate_raw_spline(alpha, beta, gamma, delta, x, n), x, n)
