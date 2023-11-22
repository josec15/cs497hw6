# cs497hw6

## Question 1
To solve this problem, we will be using dfs to traverse the graph and create an adjacency list, using
a dictionary to store the edges. We use a for loop to append each node in the graph to the dictionary.
In the dfs function, we state the base case which checks if the start node is equal to the end node then 
we are already at the node we want to be at, therefore a path exists. If we have not yet visited the node, then we will add the node to the visited set and check its neighbors to find the destination node. If the destination node is found then we can return true.
Time complexity = O(n), n represents number of edges
Space complexity = O(n + m), n represents number of edges and m represents number of nodes.

## Question 2

