import numpy as np
from src.creator.base import BaseSplineCreator


class PeriodicSplineCreator(BaseSplineCreator):

    def get_m(self, **kwargs):
        n = kwargs['n']
        h = kwargs['h']
        f = kwargs['f']
        ni = kwargs['ni']
        mi = kwargs['mi']
        lambd = kwargs['lambd']
        A = np.zeros((n, n))  # matrix for moments calculating
        B = np.zeros(n)  # free coefficients in system

        # conditions at the border for this type of spline, ni[0] is actually ni_1, mi[0] is actually mi_1
        A[0] = np.hstack((np.array((2, ni[0])), np.zeros((n - 3)), np.array((mi[0]))))

        for i in range(1, n-1):  # from 1 to n-2 (in total n - 2)
            A[i] = np.hstack((np.zeros((i - 1)), np.array((mi[i], 2, ni[i])), np.zeros((n - i - 2))))

        ni_n = h[1]/(h[-1] + h[1])
        mi_n = 1 - ni_n

        A[-1] = np.hstack((ni_n, np.zeros((n - 3)), np.array((mi_n, 2))))

        # all equations, except the first and last equation
        for i in range(0, n - 1):  # from 0 to n-2 (in total n - 1)
            B[i] = lambd[i]  # here we are typing lambda1, lambda2,.. lambda(n-1)

        B[-1] = 6 / (h[-1] + h[1]) * ((f[1] - f[-1]) / h[1] - (f[-1] - f[-2]) / h[-1])

        # moments
        M = np.linalg.solve(A, B)

        # here M[0] = M[n] and we add the last element at the beginning of the list of moments
        ret_value = []
        ret_value.append(M[-1])
        for x in M:
            ret_value.append(x)

        return ret_value
