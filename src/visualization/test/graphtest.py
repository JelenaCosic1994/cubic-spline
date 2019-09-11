from src.visualization import graph
from src.creator.complete import CompleteSplineCreator
import numpy as np

spline_creator = CompleteSplineCreator()

t = np.array([[0, 1, 2], [1, 2, 3]])
fp = np.array([[0, 2], [0, -1]])

graph.plot_spline(spline_creator.cubic_spline(t, fp=fp))
graph.plot_points(t)
graph.show_plot()
