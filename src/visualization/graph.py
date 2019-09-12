import matplotlib.pyplot as plt
import numpy
import copy

STEP = 0.01


def plot_spline(spline):
    """
    This method draw the spline
    :param spline: spline
    :return: spline graph
    """
    array_for_plotting = []
    for interval_and_function in spline.get_ranges_and_functions():
        interval = interval_and_function['range']
        function_on_interval = interval_and_function['function']
        x = numpy.arange(interval[0], interval[1] + STEP, STEP)
        array_for_plotting.append(copy.deepcopy(x))
        array_for_plotting.append(function_on_interval(array_for_plotting[-1]))
    plt.plot(*array_for_plotting)


def plot_points(table):
    """
    This method draws the points
    :param table: contains x and f(x) values
    :return: graph with points
    """
    plt.plot(table[0], table[1], 'o')


def show_plot():
    plt.show()


