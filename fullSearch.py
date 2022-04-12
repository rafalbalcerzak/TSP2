import numpy as np
import time

class Dfs():
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


class Bfs():
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

    def silnia(self,n):
        if n > 1:
            return n * self.silnia(n - 1)
        return 1

    def find_paths(self, start=0, path=None, cost=0):
        if self.paths == []:
            for i in range(len(self.matrix)):
                if i != start:
                    self.paths.append([start, i])

        while len(self.paths[0]) < len(self.matrix):
            step = len(self.paths)
            for i in range(step):
                for j in range(len(self.matrix)):
                    if j not in self.paths[i]:
                        new_path = self.paths[i].copy()
                        new_path.append(j)
                        self.paths.append(new_path)

            for i in range(step):
                self.paths.pop(0)
        for p in self.paths:
            p.append(start)


