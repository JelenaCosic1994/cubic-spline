from src.spline.spline import Spline
from src.visualization.graph import plot_spline
from src.creator.creator import cubic_spline_complete
import numpy as np

s = Spline()
# s.add_cubic_polynomial_for_range(CubicPolynomial(0, 0, 1, 0), 0, 5)
# s.add_cubic_polynomial_for_range(CubicPolynomial(0, 0, 0, 5), 5, 10)
# s.add_cubic_polynomial_for_range(CubicPolynomial(0, 1, 0, 0), 10, 15)


t = np.array([[0, 1, 2], [1, 2, 3]])
fp = np.array([[0, 2], [0, -1]])

plot_spline(cubic_spline_complete(t, fp))

# p je tacka u kojoj trazimo vrednost splajna, u zavisnosti od toga u kom je intervalu taj ce se splajn koristiti
# def KubniSplajn(p):
#     t = np.array([[0, 1, 2], [1, 2, 3]])  # funkcija zadata tablicno, vrednostima u tri cvora: 0, 1 i 2
#     fp = np.array([[0, 2], [0, -1]])  # zadate vrednosti prvog izvoda u granicnim tackama
#
#     #     t = np.array([[-2, -1.2, -0.6, 0.7, 1.8, 2.7, 3.4, 3.6], [3.9, 3.9, 4.8, 4.8, 4.3, 3.8, 2.4, 1.2]])
#     #     fp = np.array([[-2, 3.6], [0, 528]]) # nemam dat prvi izvod, vec samo fju tabelarno
#
#     x = t[0, :]
#     f = t[1, :]
#     h = np.diff(x)  # rastojanja izmedju cvorova
#
#     # hocemo vrednosti momenata u cvorovima; prvo racunamo m, n i l
#     nx = len(x)  # pp da ne znamo koliko imamo cvorova
#     m = []
#     n = []
#     l = []
#
#     for i in range(0, nx - 2):  # b=bice mi potrebno nx-1 jednacina preko m, n i l i 2 preko fp
#         m.append(h[i] / (h[i] + h[i + 1]))  # ni
#         n.append(1 - m[i])  # mi
#         l.append(6 * ((f[i + 2] - f[i + 1]) / (x[i + 2] - x[i + 1]) - (f[i + 1] - f[i]) / (x[i + 1] - x[i])) / (
#                     x[i + 2] - x[i]))  # lambda
#     print("m = ", m)
#     print("n = ", n)
#     print("l = ", l)
#
#     A = np.zeros((nx, nx))  # matrica koja ce biti matrica sistema za nalazenje momentata
#     B = np.zeros(nx)  # vektor koji ce sadrzati slobodne koeficijente sistema
#
#     #     A[0] = np.array([h[0]/3, h[0]/6, np.zeros((nx-2))]) # prva jednacina: leva strana
#     A[0] = np.hstack((np.array((h[0] / 3, h[0] / 6)), np.zeros((nx - 2))))
#     B[0] = (f[1] - f[0]) / (h[0] - fp[0][0])  # prva jednacina: desna strana
#
#     # sve ostale jednacine, osim prve i poslednje
#     for i in range(1, nx - 1):
#         #         A[i] = np.array([m[i-1], 2, n[i-1]])
#         A[i] = np.hstack((np.zeros((i - 1)), np.array([m[i - 1], 2, n[i - 1]]), np.zeros((nx - i - 2))))
#         B[i] = l[i - 1]
#
#     A[-1] = np.hstack((np.zeros((nx - 2)), np.array([h[-1] / 6, h[-1] / 3])))  # poslednja jednacina: leva strana
#     B[-1] = np.array([fp[-1][-1] - (f[-1] - f[-2]) / h[-1]])  # poslednja jednacina: desna strana
#
#     print("A = ", A)
#     print("B = ", B)
#
#     # momenti
#     M = np.linalg.solve(A, B)
#
#     print("M = ", M)
#
#     # sad trazimo splajn na pojedinacnim intervalima; prvo racunamo a, b, c, i d
#     a = []
#     b = []
#     c = []
#     d = []
#     for i in range(0, nx - 1):
#         a.append(f[i])
#         b.append((f[i + 1] - f[i]) / h[i] - h[i] / 6 * (2 * M[i] + M[i + 1]))
#         c.append(1 / 2 * M[i])
#         d.append(1 / (6 * h[i]) * (M[i + 1] - M[i]))
#
#     print("a = ", a)
#     print("b = ", b)
#     print("c = ", c)
#     print("d = ", d)
#
#     # sad racunamo splajn
#     S = []
#     for i in range(0, nx - 1):
#         S1 = []  # uz a
#         S2 = []  # uz b
#         S3 = []  # uz c
#         S4 = []  # uz d
#         S1 = np.hstack((np.zeros(nx), np.array(a[i])))
#         S2 = np.hstack((np.zeros(nx - 1), np.array((b[i], -b[i] * x[i]))))
#         S3 = np.hstack((np.zeros(nx - 2), np.array((c[i], -2 * c[i] * x[i], c[i] * x[i] ** 2))))
#         S4 = np.hstack((np.zeros(nx - 3), np.array((d[i], -d[i] * x[i], d[i] * x[i] ** 2, -d[i] * math.pow(x[i], 3)))))
#         #         print("s1 = ", S1)
#         #         print("s2 = ", S2)
#         #         print("s3 = ", S3)
#         #         print("s4 = ", S4)
#         S.append(S1 + S2 + S3 + S4)
#
#     print("Ceo splajn: ", S)
#
#     # racunamo vrednost splajna u zadatoj tacki
#     for i in range(0, nx - 1):
#         if p >= x[i] and p <= x[i + 1]:  # provera u kom intervalu se nalazi tacka
#             print("Interval: ", x[i], x[i + 1])
#             print("Splajn koji odgovara ovom intervalu: ", S[i])
#             q = np.polyval(S[i], p)  # racunanje vrednosti polinoma S[i] u tacki p
#
#     print("Vrednost kubnog splajna u datoj tacki je:", q)
#
#
# KubniSplajn(0.5)
    # crtamo tacke
    # plt.plot(x, f, 'o', color='blue')
    # res = []
    # for i in range(0, nx - 1):
    #     res.append(np.polyval(S[i], x[i]))
    #
    # res.append(np.polyval(S[1], 2))
    # print("x = ", x)
    # print("rezultat: ", res)
    # plt.plot(x, res, color='red')
    #
    # sp = np.linspace(0, 2, 100)
    #
    # plt.show()