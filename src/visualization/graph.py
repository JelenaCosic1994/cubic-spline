import matplotlib.pyplot as plt
import numpy
import copy

from src.spline.spline import Spline

STEP = 0.01


def plot_spline(spline):
    array_for_plotting = []
    for interval_and_function in spline.get_ranges_and_functions():
        interval = interval_and_function['range']
        function = interval_and_function['function']
        x = numpy.arange(interval[0], interval[1] + STEP, STEP)
        array_for_plotting.append(copy.deepcopy(x))
        array_for_plotting.append(function(array_for_plotting[-1]))
    plt.plot(*array_for_plotting)
    plt.show()
