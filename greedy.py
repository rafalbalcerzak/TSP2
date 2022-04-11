def greedy(adj_matrix, start, cost=0, visited=None):
    if visited is None:
        visited = []
    current_cost = float("inf")
    current_node = None

    if len(visited) == len(adj_matrix):
        return cost, visited

    for city in range(len(adj_matrix)):
        if city != start and city not in visited:
            if adj_matrix[start][city] <= current_cost:
                current_cost = adj_matrix[start][city]
                current_node = city

    cost = cost + current_cost
    visited.append(current_node)

    cost, visited = greedy(adj_matrix, current_node, cost, visited)

    return cost, visited

def greedy_min(adj_matrix, start):
    visited = [start]

    cost, visited = greedy(adj_matrix, 0, 0, visited)
    cost += adj_matrix[visited[-1]][start]

    visited.append(start)

    return cost, visited
