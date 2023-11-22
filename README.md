# cs497hw6

## Question 1
To solve this problem, we will be using dfs to traverse the graph and create an adjacency list, using
a dictionary to store the edges. We use a for loop to append each node in the graph to the dictionary.
In the dfs function, we state the base case which checks if the start node is equal to the end node then 
we are already at the node we want to be at, therefore a path exists. If we have not yet visited the node, then we will add the node to the visited set and check its neighbors to find the destination node. If the destination node is found then we can return true.
Time complexity = O(n), n represents number of edges
Space complexity = O(n + m), n represents number of edges and m represents number of nodes.

## Question 2


## Question 3
For this problem, we begin by creating an adjacency list that represents the graph and populates the list with a for loop that iterates over the connections list and adds both city1 and city2 and the costs. Then we initialize a total cost, prioritu queue and visited set for all visited cities to avoid loops. The main while loop will continue as long as the priority queue is not empty. While not empty, we pop the minimum cost element from the pq and if the current city has not been visited we want to add it to the visited set and add the cost to the total cost. Once all cities have been visited, we want to return the total cost. We also want to push the neighbor of the current city to the priority queue and will loop back to the top of the while loop until all cities have been visited. Return -1 if there are cities not visited which means it is not possible to connect all cities.
Time complexity = O(mlogn), where m represents the number of cities and logn is the heap operations.
Space complexity = O(m + n), since we create an adjacency list and visited set, and use a priority queue. 
