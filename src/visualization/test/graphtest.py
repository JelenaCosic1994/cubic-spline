from src.visualization.graph import plot_spline
from src.creator.complete import CompleteSplineCreator
import numpy as np

spline_creator = CompleteSplineCreator()

t = np.array([[0, 1, 2], [1, 2, 3]])
fp = np.array([[0, 2], [0, -1]])

plot_spline(spline_creator.cubic_spline(t, fp))
