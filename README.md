# CS 170 Fall 2019 Project, TeamFAV

Collaborators: https://github.com/vaibhavrdbhat, https://github.com/farhanchowdhury

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
x1x1xx1 
1xx1xxx 
xxx1xxx 
111x111 
xxx1xxx 
xxx1xxx 
1xx1xxx 

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
2 n−1 |H|−1 3·∑lui−1ui+ ∑dbjhj
i=1 j=0
Note that the 2 factor in the first term comes from the fact that the car driver expends 2 the amount of energy as a TA.
