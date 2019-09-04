from src.spline.cubic import CubicPolynomial
from src.spline.spline import Spline
from src.visualization.graph import plot_spline

s = Spline()
s.add_cubic_polynomial_for_range(CubicPolynomial(0, 0, 1, 0), 0, 5)
s.add_cubic_polynomial_for_range(CubicPolynomial(0, 0, 0, 5), 5, 10)
s.add_cubic_polynomial_for_range(CubicPolynomial(0, 1, 0, 0), 10, 15)
plot_spline(s)
