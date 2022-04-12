import numpy as np
import time

class dfs():
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.paths = []
        self.shortest = None
        self.longest = None
        self.time = None
        self.start_time = 0

    def get_col(self, x):
        row = self.matrix[:,x]
        return row

    def get_row(self, x):
        return self.matrix[x]

    def find_paths(self, start=0, path=None, cost=0):
        if path is None:
            path = [start]
            self.start_time = time.perf_counter()
        if len(path) == len(self.matrix):
            row = self.get_row(start)
            if row[path[0]] != float("inf"):
                path.append(path[0])
                new_cost = cost + row[path[0]]
                self.paths.append((new_cost, path))
                return
            return

        row = self.get_row(start)
        for i in range(len(row)):
            if i not in path:
                if row[i] != float("inf"):
                    new_path = path.copy()
                    new_path.append(i)
                    new_cost = cost+row[i]
                    self.find_paths(i, new_path, new_cost)

        if len(self.paths)>0:
            self.paths.sort(key=lambda i: i[0])
            self.shortest = self.paths[0]
            self.longest = self.paths[-1]
        self.time = time.perf_counter() -self.start_time

