# Question 4
# All Paths From Source to Target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from
# node 0 to n - 1 and return them in any order. The graph is given as follows: graphs[i] is a list of all
# nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

def allPathsFromSourceToTarget(graph):
    end_node = len(graph) - 1
    def dfs(node, path, result):
        if node == end_node:
            result.append(path)
        for neighbor in graph[node]:
            dfs(neighbor, path + [neighbor], result)
    result = []
    dfs(0, [0], result)
    return result

graph = [[1,2],[3],[3],[]]
print(allPathsFromSourceToTarget(graph))