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

otherexample = [
    [1,2],
    [0,2,6],
    [],
    [6],
    [3,5],
    [4],
    [5]
]

visited = set([])
ans = ''
def dfs(neighbors, start):
    global ans
    to_check = [start]
    visited.add(start)
    while len(to_check) > 0:
        next = to_check.pop()
        # print(f"Considering neighbors of {next}")
        # fstring 类似js中的${}
        for n in neighbors[next]:
            # print(f"Looking at {n}")
            if n not in visited:
                ans = ans + f"{n},"
                visited.add(n)
                to_check.append(n)

    return visited

import json
with open('connectgraph.json') as f:
    mymaze = json.load(f)


for d in range(0,len(mymaze)):
    if len(visited) < len(mymaze):
        ans = '{'
        dfs(mymaze,d)
        ans = ans + '}'
        print(ans)