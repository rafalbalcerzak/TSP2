import random
import matplotlib.pyplot as plt
import numpy as np
import fullSearch
import greedy


"""
1. dfs (1/1)
2. bfs (1/1)
3. greedy najbliższego sąsiada (1/1)
4. greedy własny (0/1)
5. mechanizm nawrotów (0/1)
    -algorytm A*
    -porównać heurystyki:
        -minimalną 
        -średnią, powinna być szybsza


"""
"""
od zbioru wszsytkich dróg, odejmuje odwiedzone (G-V-NR), średnią i min wyliczam z pozostałych dróg?
c = k + h
h=n *f(k)
k->zbiór dostępnych krawędzi
f->{avg,min}
"""
size = 5
start_city = 0
allRoads = False
symmetrical = False
INT_MAX = 2147483647


def euclidean(x, y):
    return ((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2 + (y[2] - x[2]) ** 2) ** (1 / 2)


def city_generator():
    return [random.randint(-100, 100), random.randint(-100, 100), random.randint(0, 50)]


def city_distance(x, y):
    if allRoads:
        if symmetrical:
            return euclidean(x, y)
        else:
            if x[2] > y[2]:
                return euclidean(x, y) * 0.9
            elif x[2] < y[2]:
                return euclidean(x, y) * 1.1
            else:
                return euclidean(x, y)

    else:
        if symmetrical:
            return euclidean(x, y) if random.randint(0, 100) <= 80 else float("inf")
        else:
            if x[2] > y[2]:
                return euclidean(x, y) * 0.9 if random.randint(0, 100) <= 80 else float("inf")
            elif x[2] < y[2]:
                return euclidean(x, y) * 1.1 if random.randint(0, 100) <= 80 else float("inf")
            else:
                return euclidean(x, y) if random.randint(0, 100) <= 80 else float("inf")


def adjacency_matrix_generator(vertices_list):
    adjacency_matrix = list()

    for vertices in vertices_list:
        matrix_row = list()
        for j in vertices_list:
            if vertices == j:
                matrix_row.append(float("inf"))
            else:
                matrix_row.append(city_distance(vertices, j))
        adjacency_matrix.append(matrix_row)
    return adjacency_matrix


def roads(adj_matrix):
    all_roads = size ** 2
    allPossible = size * (size - 1)  # miasta nie są połączone same ze sobą
    allInf = sum(a.count(float("inf")) for a in adj_matrix)
    return ((all_roads - allInf) / allPossible) * 100


if __name__ == '__main__':
    # generowanie miast
    cities = []
    for i in range(0, size):
        cities.append(city_generator())


    matrix = adjacency_matrix_generator(cities)

    print("Adjacency matrix:")
    for row in matrix:
        print('\t'.join([str(round(x, 1)).rjust(4) for x in row]))

    print("Available roads: " + str(round(roads(matrix), 2)) + "%")

    dfs = fullSearch.Dfs(matrix)
    dfs.find_path(start_city)

    bfs = fullSearch.Bfs(matrix)
    bfs.find_path(start_city)

    nn = greedy.NN(matrix)
    nn.find_path(start_city)

    print(f'Liczba wszystkich tras: {len(bfs.paths)}')
    print(f'Liczba dostępnych tras: {len(dfs.paths)}')
    print('=================================================')

    algorithms = [['DFS: ', dfs.time, dfs.shortest[0], dfs.shortest[1]],
                  ['BFS', bfs.time, bfs.shortest[0], bfs.shortest[1]],
                  ['NN:', nn.time, nn.path[0], nn.path[1]]]

    print('Algorytm: |Czas    |Koszt  |Scieżka')
    print('----------+--------+-------+' + '-' * size * 4)
    for row in algorithms:
        print(f'{row[0]:10}|{row[1]:7.2E}|{row[2]:6.2f} | {row[3]}')

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    c = np.array(cities)
    ax.scatter(c[:, 0], c[:, 1], c[:, 2])

    path = dfs.shortest[1]
    for i in range(len(path)-1):
        cn = path[i]
        ncn = path[i+1]
        ax.plot([cities[cn][0], cities[ncn][0]],
                [cities[cn][1], cities[ncn][1]],
                [cities[cn][2], cities[ncn][2]],
                c='red')
    plt.show()


