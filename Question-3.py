# Question 3
# Connecting Cities with minimum Cost

# There are n cities numbered from 1 to n. You are given connections, where each connection[i] == [city1, city2, cost]
# represents the cost to connect city1 and city2 together. (A connection is bidirectional: connecting city1 and city2
# is the same as connecting city2 and city1.) Return the minimum cost so that for every pair of cities, there
# exists a path of connections (possibly of length 1) that connects those two cities together. The cost is the sum
# of the connection costs used. If the task is impossible, return -1.

from collections import defaultdict
import heapq
def minCostToConnect(n, connections):
    adjList = defaultdict(list)
    for c1, c2, cost in connections:
        adjList[c1].append([cost, c2])
        adjList[c2].append([cost, c1])
    total_cost = 0
    pq = [[0,n]]
    visited = set()
    while pq:
        curr_cost, curr_city = heapq.heappop(pq)
        if curr_city not in visited:
            visited.add(curr_city)
            total_cost += curr_cost
        if len(visited) == n:
            return total_cost
        while adjList[curr_city]:
            [aCost, aCity] = adjList[curr_city].pop()
            heapq.heappush(pq, [aCost, aCity])
    return -1

n = 3
connections = [[1,2,5],[1,3,6],[2,3,1]]
print(minCostToConnect(n, connections))