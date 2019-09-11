import numpy as np
import math
from src.spline.spline import Spline
from abc import ABC, abstractmethod


class BaseSplineCreator(ABC):

    @abstractmethod
    def get_a_and_b(self):
        pass

    def cubic_spline(self, t, fp):

        x = t[0, :]  # (ima duzinu n + 1) x0, x1, x2,.. xn
        f = t[1, :]  # (ima duzinu n + 1) x0, x1, x2,.. xn
        h = [None] + list(np.diff(x))  # rastojanja izmedju cvorova (ima duzinu n + 1), nulti element se ne koristi,
        #  dodat zbog lakseg indeksiranja

        n = len(x) - 1  # x0, x1,.. xn (n je n iz indeksa xn)

        ni = [None] * n  # (ima duzinu n) nulti element dodat zbog lakseg indeksiranja
        mi = [None] * n  # (ima duzinu n) nulti element dodat zbog lakseg indeksiranja
        lambd = [None] * n  # (ima duzinu n) nulti element dodat zbog lakseg indeksiranja

        for i in range(1, n):  # 1, 2,.. n-1
            ni[i] = h[i+1] / (h[i] + h[i+1])
            mi[i] = 1 - ni[i]
            lambd[i] = (6/(h[i] + h[i+1]))*((f[i+1] - f[i])/h[i+1] - (f[i] - f[i-1])/h[i])

        print("Mi: ", mi)
        print("Ni: ", ni)
        print("Lambda: ", lambd)
        mi = mi[1:]
        ni = ni[1:]
        lambd = lambd[1:]

        A, B = self.get_a_and_b()

        # momenti
        M = np.linalg.solve(A, B)

        print("M = ", M)

        # sad trazimo splajn na pojedinacnim intervalima; prvo racunamo a, b, c, i d
        alpha = []
        beta = []
        gamma = []
        delta = []
        for i in range(0, n):
            alpha.append(f[i])
            beta.append((f[i + 1] - f[i]) / h[i+1] - h[i+1] / 6 * (2 * M[i] + M[i + 1]))
            gamma.append(1 / 2 * M[i])
            delta.append((1 / (6 * h[i+1])) * (M[i + 1] - M[i]))

        print("alpha = ", alpha)
        print("beta = ", beta)
        print("gamma = ", gamma)
        print("delta = ", delta)
    #
        # sad racunamo splajn
        S = []
        for i in range(0, n):
            S1 = np.hstack((np.zeros(n+1), np.array(alpha[i])))
            S2 = np.hstack((np.zeros(n), np.array((beta[i], -beta[i] * x[i]))))
            S3 = np.hstack((np.zeros(n - 1), np.array((gamma[i], -2 * gamma[i] * x[i], gamma[i] * x[i] ** 2))))
            S4 = np.hstack((np.zeros(n - 2), np.array((delta[i], -3 * delta[i] * x[i], 3 * delta[i] * x[i] ** 2, -delta[i] * math.pow(x[i], 3)))))

            S.append(S1 + S2 + S3 + S4)

        print("Ceo splajn: ", S)

        spline = Spline()

        for i in range(0, n):
            x1 = x[i]
            x2 = x[i+1]
            spline_coefs = S[i]

            spline.add_cubic_polynomial_for_range(spline_coefs, x1, x2)

        return spline
