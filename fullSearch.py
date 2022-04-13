import numpy as np
import time


class Dfs:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.paths = []
        self.shortest = None
        self.longest = None
        self.time = None
        self.start_time = 0

    def get_col(self, x):
        row = self.matrix[:, x]
        return row

    def get_row(self, x):
        return self.matrix[x]

    def find_path(self, start=0, path=None, cost=0):
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
                    new_cost = cost + row[i]
                    self.find_path(i, new_path, new_cost)

        if len(self.paths) > 0:
            self.paths.sort(key=lambda pathd: pathd[0])
            self.shortest = self.paths[0]
            self.longest = self.paths[-1]
        self.time = time.perf_counter() - self.start_time


class Bfs:
    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.paths = []
        self.shortest = None
        self.longest = None
        self.time = None
        self.start_time = 0

    def get_col(self, x):
        row = self.matrix[:, x]
        return row

    def get_row(self, x):
        return self.matrix[x]

    def find_path(self, start=0):
        self.start_time = time.perf_counter()
        if not self.paths:
            for i in range(len(self.matrix)):
                if i != start:
                    row = self.get_row(start)
                    new_cost = row[i]
                    self.paths.append([new_cost, [start, i]])

        while len(self.paths[0][1]) < len(self.matrix):
            step = len(self.paths)
            for i in range(step):
                for j in range(len(self.matrix)):
                    if j not in self.paths[i][1]:
                        new_path = self.paths[i][1].copy()
                        new_path.append(j)
                        row = self.get_row(self.paths[i][1][-1])
                        new_cost = self.paths[i][0] + row[j]
                        self.paths.append([new_cost, new_path])

            for i in range(step):
                self.paths.pop(0)

        for p in self.paths:
            row = self.get_row(p[1][-1])
            new_cost = row[start]
            p[0] = p[0] + new_cost
            p[1].append(start)

        self.paths.sort(key=lambda pathb: pathb[0])
        self.shortest = self.paths[0]
        self.longest = self.paths[-1]

        self.time = time.perf_counter() - self.start_time
