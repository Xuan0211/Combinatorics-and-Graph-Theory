shortest_path = {
    'A': {'B': 2, 'C': 9, 'D': 4},
    'B': {'A': 2, 'C': 5, 'E': 10, 'F': 2},
    'C': {'A': 9, 'D': 2, 'E': 11, 'B': 5},
    'D': {'A': 4, 'C': 2, 'E': 7},
    'E': {'B': 10, 'G': 1, 'D': 7},
    'F': {'B': 2, 'G': 2, 'H': 3},
    'G': {'E': 1, 'F': 2, 'H': 1},
    'H': {'F': 3, 'G': 1}
}

start = 'A'

def findClosestNode(distances, to_check):
    m = -1
    node = -1
    for v in to_check:
        if m == -1 or distances[v] < m:
            node = v
            m = distances[v]
    return node


def find_shortest_paths(graph, start):
    to_check = set([start])
    visited = set([start])
    distances = {start: 0}
    paths = {start: [start]}


    while len(to_check) > 0:
        next = findClosestNode(distances, to_check)
        to_check.remove(next)
        visited.add(next)
        print(f"Considering neighbors of {next}")
        for n in graph[next].keys():
            print(f"Looking at {n}")
            if n not in visited:
                print(f"Not found shortest distance to {n} yet")
                new_distance = distances[next] + graph[next][n]
                if n in distances:
                    if new_distance < distances[n]:
                        print(f"Found new shortest path to {n} of length {new_distance}")
                        print(f"Replacing {paths[n]} with {paths[next] + [n]}")
                        distances[n] = new_distance
                        paths[n] = paths[next] + [n]
                    else:
                        print(f"Found a longer path to {n} of length {new_distance}")
                        print(f"Not replacing {paths[n]} with {paths[next] + [n]}")

                else:
                    print(f"Found first path to {n}")
                    print(f"Path is {paths[next] + [n]}")
                    distances[n] = new_distance
                    paths[n] = paths[next] + [n]
                to_check.add(n)

    return {'distances': distances, 'paths': paths}

print(find_shortest_paths(shortest_path, 'A'))
