__author__ = 'vlad'

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Algorithm(object):
    def __init__(self, init_point, function):
        self.points = [np.array(init_point, ndmin=1, dtype=float)]
        self.dimension = len(self.points[0])
        self.function = function
        try:
            function.val(self.points[0])
        except Exception as ex:
            raise Exception('Failed calculating init point value', ex)


    def iteration(self):
        pass

    def launch(self):
        pass

    def _get_mask(self):
        return '#{number:<7} x: {point}\nf: {value}\n'

    def _generate_strings(self):
        mask = self._get_mask()
        for number in range(len(self.points)):
            point = self.points[number]
            yield mask.format(number=number, point=str(point), value=self.function.val(point))

    def print_to_file(self, filename):
        file = open(filename, 'w')
        file.writelines(self._generate_strings())
        file.close()


    def plot_graph(self, color='r', alpha=0.6):
        """
        works for 2-dimensional only
        """
        if self.dimension != 2:
            raise Exception('Bad idea')
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y = np.transpose(self.points)
        z = list(map(self.function.val, self.points))
        ax.scatter(x, y, z, c=color, alpha=alpha)
        plt.show()