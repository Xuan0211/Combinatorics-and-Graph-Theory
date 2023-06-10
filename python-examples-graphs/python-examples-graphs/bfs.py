maze = [
    [],
    [2,6],
    [1,3],
    [2,8],
    [9,5],
    [4,10],
    [1,7],
    [6],
    [3,13],
    [4,14],
    [5,15],
    [12],
    [11,13],
    [8,12,14],
    [13,9,15],
    [14,10]
]

other_example = [
    [1,2],
    [0,2,6],
    [],
    [6],
    [3,5],
    [4],
    [5]
]



def bfs(neighbors, start):
    to_check = [start]
    visited = set([start])
    while len(to_check) > 0:
        next = to_check.pop(0)
        print(f"Considering neighbors of {next}")
        for n in neighbors[next]:
            print(f"Looking at {n}")
            if n not in visited:
                print(f"Not seen {n} before")
                visited.add(n)
                to_check.append(n)

    return visited

bfs(maze, 3)