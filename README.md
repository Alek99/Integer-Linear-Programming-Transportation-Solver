# CS 170 Fall 2019 Project, TeamFAV

Collaborators:
Bhat, Vaibhav @ https://github.com/vaibhavrdbhat  
Chowdhury, Farhan @ https://github.com/farhanchowdhury  

# CS 170 Efficient Algorithms and Intractable Problems Fall 2019 P. Raghavendra and S. Rao

# Problem Statement
Professor Rao and his army of TAs are working in Soda Hall late at night, writing the final exam for CS 170. Rao offers to drive and drop TAs off closer to their homes so that they can all get back safe despite the late hours. However, the roads are long, and Rao would also like to get back to Soda as soon as he can. Can you plan transportation so that everyone can get home as efficiently as possible?

Formally, you are given an undirected graph G = (L,E) where each vertex in L is a location. You are also given a starting location s, and a list H of unique locations that correspond to homes. The weight of each edge (u,v) is the length of the road between locations u and v, and each home in H denotes a location that is inhabited by a TA. Travel- ing along a road takes energy, and the amount of energy expended is proportional to the length of the road. For every unit of distance traveled, the driver of the car expends 2 units of energy, and a walking TA expends 1 unit of energy.

You must return a list of vertices vi that is the tour taken by the car (cycle with repetitions allowed), as well as a list of drop-off locations at which the TAs get off. You may only drop TAs off at vertices visited by the car, and multiple TAs can be dropped off at the same location.

We’d like you to produce a route and sequence of drop-offs that minimizes total energy expenditure, which is the sum of Rao’s energy spent driving and the total energy that all of the TAs spend walking. Note TAs do not expend any energy while sitting in the car. You may assume that the TAs will take the shortest path home from whichever location they are dropped off at.

# Input Format
The first line of the input should contain a single integer, which equals the number of locations, |L|. The second line should also be an integer, which equals the number of homes, |H|. The third line should be a list of distinct names, separated by spaces. These are the names of your locations, L. The names must be alphanumeric, can contain up to 20 characters, and can contain only characters A-Z, a-z, and 0-9. The fourth line must be a list of names, separated by spaces, that are the names of your homes, H. All the homes need to be contained in the location list on the previous line. In other words H should be a subset of L. The fifth line must be the name of the location that is your starting point. Your output does not need to specify the walking paths of the TAs; we assume the TAs know how to find the shortest path home.

The next |L| lines should contain an adjacency matrix representation of your graph. Location i refers to the location name at index i of L. For example, in the sample input shown below, location 2 refers to Wheeler. If there is no road between two locations i and j on the map, then the corresponding entry in the adjacency matrix, Mij, should be the lowercase ‘x’. For i = j, the entry Mi j should also be ‘x’, as there should not be a road from a location to itself. If there is a road between i and j, the entry Mi j should be the length of that road, li j . The li j must be strictly positive integers or floating-point numbers. They must be less than 2 billion, and floats must have at most 5 decimal places. It must be the case that li j = l ji for all values of i and j, since the graph is undirected. In other words, your adjacency matrix must be symmetric.
  3
The car must start and end at s, and every TA must return to their home in H.
CS 170, Fall 2019 1

For any two i, j, let d(i, j) be the length of the shortest path between i and j. Your graph must be connected and the edge weights must obey the triangle inequality. This means that for any two vertices u and v such that the edge (u, v) is in your graph, the shortest path to get from u to v needs to be the edge (u, v), and not a path through any of the other vertices.
As an equivalent condition, for all u, v, w ∈ L where (u, v) ∈ E :
luv ≤d(u,w)+d(w,v)
Additionally, it must be that lii = 0 (in the case of our input, we will have an ‘x’ present) and li j ̸= 0 when i ̸= j. 

Sample input:
7  
4  
Soda Dwinelle Wheeler Campanile Cory RSF Barrows Wheeler Campanile Cory RSF  
Soda  
x 1 x 1 x x 1   
1 x x 1 x x x    
x x x 1 x x x   
1 1 1 x 1 1 1   
x x x 1 x x x   
x x x 1 x x x   
1 x x 1 x x x    

# Output Format
The output file corresponding to an input must have the same name, except with the extension replaced by ".out". For example, the output file for "1.in" must be named "1.out".

Your output should contain the cycle the car took, the number of distinct locations at which TAs were dropped off, and the homes of the TAs who got off at each drop-off location. The first line should be a space-separated list of location names which represents the route taken by the car in your solution. These locations should be in the order in which they are visited and the list must start and end with the starting location defined in the corresponding input file. Locations may be repeated. The second line should contain the number of drop-off locations.

Each line in the rest of the output file should be a list of locations, the first of which corresponds to the drop-off location and the rest of which correspond to the homes of the TAs who were dropped off at that location. For example, if Julia lives in Cory and was dropped off at Soda, and Neha lives in the Campanile and was dropped off at the Campanile, we should have the two lines ’Soda Cory’ and ’Campanile Campanile’. The order in which these lines appear in the output file does not matter. If no TAs get off at a location, it should not be included. If multiple TAs get off at the same location, they should all be included on one line. For example, if Dee and Emaan were both dropped off at Dwinelle, and Dee lives in Wheeler and Emaan lives in the RSF, one of the lines in the output file would be ’Dwinelle Wheeler RSF’.

In the sample output below, the TA who lives in Cory is dropped off at Soda, the TAs who live in Wheeler and the RSF are dropped off at Dwinelle, and the TA who lives in the Campanile is dropped off at the Campanile.
Sample output:

Soda Dwinelle Campanile Barrows Soda  
3  
Soda Cory  
Dwinelle Wheeler RSF  
Campanile Campanile  

# Submission Evaluation
Your score on a particular output will be determined by the sum of the energy it takes the car to drive the route and the total energy it takes for all the TAs to walk home. You may assume that the TAs will take the shortest path home from whichever location they are dropped off at. Formally, let the path of the car be u0 . . . un−1 where u0 = un−1 = s, let b j be the location you drop off the j-th TA, and let h j be that TA’s home. Let li j be the length of the road between locations i and j (which must be adjacent), and di j be the shortest path distance between locations i and j (which need not be adjacent). Your score is given by:

![alt text](https://github.com/Alek99/Integer-Linear-Programming-Transportation-Solver/blob/master/Screen%20Shot%202019-12-17%20at%2012.50.20%20AM.png)  

Note that the 2 factor in the first term comes from the fact that the car driver expends 2 the amount of energy as a TA.

# TeamFav's Solution
# Modification of Christofides’ Algorithm
implementing a solution to this problem span Christofides’ Approximation algorithm for Traveling Salesman Problem (if such a reduction for Traveling Salesman is found to be useful). We believe this algorithm to be sound when finding an approximate cyclic path of the car ride as it approximates the optimal solution by a factor of 3/2.
As Traveling Salesman is run on a complete graph we would add the missing edges by calculating a heuristic determined by the all-pairs shortest paths algorithm. We believe this heuristic to be good in order to account for and minimize walking distance given the dropoff location. If there exists a Hamiltonian cycle of locations that covers at least one location corresponding to a shortest path pair (either a TA’s home or dropoff location (a problem that can be reduced to metric TSP), a highly optimal approximate solution can be inferred.
Utilizing ILP
We took a modified ILP approach using Gurobi’s ILP solver. With Integer Linear Programming being reduced to Metric TSP, we can write the specification and proceed with the reduction accordingly:
1. The objective function would directly mirror the minimization of the cost function of the factored sum of the driver’s path and the sum of TA’s walking distance covered.
2. The linear constraints would stipulate:
a. that only one city can be visited from city 1 and that only one city is
visited at each stage of travel.
b. ensure that a given city is visited at exactly one stage of travel.
Reducing ILP to Drive the TAs Home would be useful to ensure that all homes are spanned in addition to ensuring a cyclic path exists for the driver. After reducing the ILP using the Gurobi solver we tried to come up with an efficient drop off path the driver can take.
 
  We reduced the Drive the TAs Home Problem to a modified Travelling Salesman Problem in which we cut ‘bridges’ in the graph and completing the subgraph by adding weighted edges based off of the all-pairs shortest path heuristic. The graph G is determined by the locations as the vertices and routes as the weighted edges. The graph is undirected therefore we have a symmetric matrix.
In order to keep track of the locations that can guarantee that locations that are not in the houses that have degree 1 must be deleted in order to prevent useless traversal drive. We recurse this function in order to cut longer singular stretches of road.
For all houses that have degree 1 should be cut from the graph as well as any cyclic path not including a drive to these houses will retain optimality as (2)(2⁄3)(D) total energy is greater than D.
For any locations that can only be reached by two or less locations (the edge as degree two or less), we cut the location and its two incident edges. Keeping track of the edges is important in order to further compute what we call “bridges” - location is a home with degree 2 whose edges leave two distinct connected components on both ends when cut from the graph. Another type of edge would be along a singular path to a leaf or lead to a leaf itself.
As TSP must be run on a complete graph, we add weighted edges by summing the entire row of the in-degree node, in order to avoid the TSP using these edges that are not really present.
With the remaining graph, we run the ILP subtourelim and subtour function from the Gurobi ILP on all of its completed connected components before reconnecting the “bridges”.
The ‘bridges’ are determined by checking if the edges that were cut connects two connected components.

  After implementing our ILP solution and testing it on gradescope our drivers paths turned out as not valid. For every path there was From further investigating this we could not determine where Gurobi was failing so we reverted in out naive solution. Our naive solution is similar to TSP where the driver individually drives every student to their destination. Using this naive approach we were able to score in the top 1⁄3 of outputs.
