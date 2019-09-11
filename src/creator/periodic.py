import numpy as np
from src.creator.base import BaseSplineCreator


class PeriodicSplineCreator(BaseSplineCreator):

    def get_a_and_b(self, **kwargs):
        n = kwargs['n']
        h = kwargs['h']
        fp = kwargs['fp']
        f = kwargs['f']
        ni = kwargs['ni']
        mi = kwargs['mi']
        lambd = kwargs['lambd']
        A = np.zeros((n, n))  # matrica koja ce biti matrica sistema za nalazenje momentata
        B = np.zeros(n)  # vektor koji ce sadrzati slobodne koeficijente sistema

        # granicni uslovi za ovaj tip splajna, ni[0] je u stvari ni_1, mi[0] je u stvari mi_1
        A[0] = np.hstack((np.array((2, ni[0])), np.zeros((n - 3)), np.array((mi[0]))))

        for i in range(1, n-1):  # od 1 do n-2 (ima ih n - 2)
            A[i] = np.hstack((np.zeros((i - 1)), np.array((mi[i], 2, ni[i])), np.zeros((n - i - 1))))

        ni_n = h[1]/(h[-1] + h[1])
        mi_n = 1 - ni_n

        A[-1] = np.hstack((ni_n, np.zeros((n - 3)), np.array((mi_n, 2))))

        # sve ostale jednacine, osim prve i poslednje
        for i in range(0, n - 1):  # od 0 do n-2 (ima ih n - 1)
            B[i] = lambd[i]  # ovde upisujemo lambda1, lambda2,.. lambda(n-1)

        B[-1] = 6 / (h[-1] + h[1]) * ((f[1] - f[-1]) / h[1] - (f[-1] - f[-2]) / h[-1])

        print("A=", A)
        print("B=", B)

        return A, B
