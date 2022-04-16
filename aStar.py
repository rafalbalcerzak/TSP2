import numpy as np
import time

class aStar:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.path= []
        self.time = None
        self.start_time = 0
        self.methode = 'min'

    def get_row(self, x):
        return self.matrix[x]


    def minMethode(self):

        return

    def find_path(self, start=0, path=None, methode='min'):
        self.methode = methode
        self.start_time = time.perf_counter()
        if path is None:
            self.path = [0, [start]]

        path_length = len(self.matrix)

        for c in range(len(self.matrix)):
            if c not in self.path[1]:
                if self.get_row(start)[c] != float('inf'):
                    actual_cost = self.get_row(start)[c]
                    min_cost = min(np.delete(self.matrix, c, 1))
                    remaining_cost = actual_cost + ((len(self.matrix) - len(self.path[1])) * min_cost)
                    aprox_cost = len(self.matrix) * min_cost


        if self.methode == 'min':
            row = self.get_row()


