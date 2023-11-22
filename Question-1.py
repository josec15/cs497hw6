# Question 1
# Find if Path Exists in Graph

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1
# (inclusive). The edges in the graph are represented as a 2D integer array edges, where each
# edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex start and vertex end.
# Given edges and the integers n, start, and end, return true if there is a valid path from start
# to end, or false otherwise.

from collections import defaultdict

def validPath(n, edges, start, end):
    adjList = defaultdict(list)
    for node1, node2 in edges:
        adjList[node1].append(node2)
        adjList[node2].append(node1)
    visited = set()
    def dfs(node):
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in adjList[node]:
                result = dfs(neighbor)
                if result:
                    return True
    return dfs(start)

if __name__ == "__main__":
    n1 = 3
    edges1 = [[0, 1], [1, 2], [2, 0]]
    source1 = 0
    destination1 = 2
    print(validPath(n1, edges1, source1, destination1))
    n2 = 6
    edges2 = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    source2 = 0
    destination2 = 5
    print(validPath(n2, edges2, source2, destination2))

