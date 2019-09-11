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

        # granicni uslovi za ovaj tip splajna
        A[0] = np.hstack((np.array((2, ni[0])), np.zeros((n - 3)), np.array((mi[0]))))

        B[-1] = 6 / (h[-1] + h[1]) * ((f[1] - f[-1]) / h[1] - (f[-1] - f[-2]) / h[-1])

        # sve ostale jednacine, osim prve i poslednje
        for i in range(0, n - 1):  # od 0 do n-2 (ima ih n - 1)
            B[i] = lambd[i]  # ovde upisujemo lambda1, lambda2,.. lambda(n-1)

        # dovde je odradjeno, u ni i mi treba ubaciti poslednje clanove po formuli za ovaj tip
        # u mi i ni nemamo mi_0 i mi_n imamo samo od 1 do n-1 elemente

        A[-1] = np.hstack((np.array((ni[-1])), np.zeros((n - 3)), np.array((mi[-1], 2))))

        for i in range(1, n - 1):  # od 1 do n-2 (ima ih n - 2)
            A[i] = np.hstack((np.zeros((i - 1)), np.array((mi[i - 1], 2, ni[i - 1])), np.zeros((n - i - 1))))

        print("A=", A)
        print("B=", B)

        return A, B
