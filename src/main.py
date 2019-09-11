from src.visualization import graph
from src.creator.complete import CompleteSplineCreator
from src.creator.periodic import PeriodicSplineCreator
from src.creator.second import SecondSplineCreator

import numpy as np


def main():
    spline_creator = CompleteSplineCreator()
    t = np.array([[0, 1, 2], [1, 2, 3]])
    fp = np.array([[0, 2], [0, -1]])
    graph.plot_spline(spline_creator.cubic_spline(t, fp=fp))
    graph.plot_points(t)
    graph.show_plot()

    spline_creator = PeriodicSplineCreator()
    t = np.array([[0, 1, 2, 3, 4], [1, 5, 1, 5, 1]])
    graph.plot_spline(spline_creator.cubic_spline(t))
    graph.plot_points(t)
    graph.show_plot()

    # examples used for pdf:
    spline_creator = SecondSplineCreator()
    t = np.array([[-3.7, -2.6, -0.6, 2.7, 3.9], [0.4, 2.8, 4.8, 3.8, 0]])
    graph.plot_spline(spline_creator.cubic_spline(t))
    graph.plot_points(t)
    graph.show_plot()

    spline_creator = SecondSplineCreator()
    t = np.array([[-3.7, -2, -0.6, 2.7, 3.6, 3.9], [0.4, 3.9, 4.3, 3.8, 1.2, 0]])
    graph.plot_spline(spline_creator.cubic_spline(t))
    graph.plot_points(t)
    graph.show_plot()

    spline_creator = SecondSplineCreator()
    t = np.array([[-3.7, -2, -1.2, -0.6, 0.7, 1.8, 2.7, 3.4, 3.6, 3.9], [0.4, 3.9, 3.9, 4.8, 4.8, 4.3, 3.8, 2.4, 1.2, 0]])
    graph.plot_spline(spline_creator.cubic_spline(t))
    graph.plot_points(t)
    graph.show_plot()


if __name__ == "__main__":
    main()
