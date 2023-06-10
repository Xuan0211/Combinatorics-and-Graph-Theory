import json
import string

# Function to print the path.
# Uses letters a-z for height, A-Z for height on the path.
def print_path(data, path):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i,j) in path:
                print(string.ascii_uppercase[data[i][j]],end="")
            else:
                print(string.ascii_lowercase[data[i][j]],end="")
        print("")


class Graph:
    def __init__(self, graph_data, heuristic_type):
        # Remember the graph_data and heuristic
        self.graph_data = graph_data
        self.heuristic_type = heuristic_type

    def neighbours(self, vertex):
        print("TODO: Get neighbours of vertex")

    def edge_length(self, vertex1, vertex2):
        print("TODO: Get length of an edge")

    def heuristic(self, vertex1, vertex2):
        print("TODO: Get heuristic distance between two vertices")


def find_shortest_path(graph, startnode, endnode):
    # TODO: This is not the correct path!
    return {'path': [(startnode), (endnode)], 'distance': 1, 'explored': 1 }



# Read problem file
filename = input("Enter problem filename:")
with open(filename) as f:
    data = json.load(f)

heuristic_type = input("Enter heuristic type: ")

# Go from top-left to bottom-right
startnode = (0,0)
endnode = (len(data)-1, len(data[0])-1)
graph = Graph(data, heuristic_type)

output = find_shortest_path(graph, startnode, endnode)

print("")
print("----------------------")
print(f"Search explored {output['explored']} nodes")
print(f"The shortest path is length: {output['distance']}")
print(f"The path is: {output['path']}")


print_path(data, output['path'])
