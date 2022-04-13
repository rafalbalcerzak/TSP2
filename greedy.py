import numpy as np
import time


class NN:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.path = []
        self.time = None
        self.start_time = 0

    def get_row(self, x):
        return self.matrix[x]

    def find_path(self, start=0):
        self.start_time = time.perf_counter()
        self.path = [0, [start]]

        while len(self.path[1]) < len(self.matrix):
            row = self.get_row(self.path[1][-1])
            current_cost = float("inf")
            city = None
            for c in range(len(row)):
                if c not in self.path[1]:
                    if row[c] <= current_cost:
                        current_cost = row[c]
                        city = c
            self.path[0] = self.path[0] + current_cost
            self.path[1].append(city)
        # dodatnie pounktu startowego
        row = self.get_row(self.path[1][-1])
        self.path[0] = self.path[0] + row[start]
        self.path[1].append(start)
        self.time = time.perf_counter() - self.start_time
