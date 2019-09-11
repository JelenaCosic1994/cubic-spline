import numpy as np
from src.creator.base import BaseSplineCreator


class SecondSplineCreator(BaseSplineCreator):

    def get_m(self, **kwargs):
        n = kwargs['n']
        h = kwargs['h']
        fp = kwargs['fp']
        f = kwargs['f']
        ni = kwargs['ni']
        mi = kwargs['mi']
        lambd = kwargs['lambd']

        A = np.zeros((n+1, n+1))  # matrica koja ce biti matrica sistema za nalazenje momentata
        B = np.zeros(n+1)  # vektor koji ce sadrzati slobodne koeficijente sistema


        # granicni uslovi za ovaj tip splajna
        A[0] = np.hstack((np.array((2, 0)), np.zeros((n-1))))
        A[-1] = np.hstack((np.zeros((n - 1)), np.array((0, 2))))

        B[0] = 0
        B[-1] = 0

        # sve ostale jednacine, osim prve i poslednje
        for i in range(1, n):
            A[i] = np.hstack((np.zeros((i - 1)), np.array((mi[i-1], 2, ni[i-1])), np.zeros((n - i - 1))))
            B[i] = lambd[i-1]

        print("A=", A)
        print("B=", B)

        # momenti
        M = np.linalg.solve(A, B)

        print("M = ", M)

        return M
