file = open(input, "r")

numloc = int(file.readline())
numhouse = int(file.readline())

locations = file.readline().split()

houses = file.readline().split()

startingVertex = file.readline()

graph = []

adjMatrix = {}
editedMatrix = {}
adjText = {}
for loc in locations:
	adjMatrix[loc] = {} 
	adjRow = file.readline()
	graph.append(adjRow.split())
	adjText[loc] = adjRow
	for i, adjDistance in enumerate(adjRow.split()):
		if (adjDistance is not 'x'):
			adjDistance = float(adjDistance)
		adjMatrix[loc][locations[i]] = adjDistance

V = numloc
INF = 999999
for i in range(len(graph)):
	graph[i][i] = 0
for j, arr in enumerate(graph):
	for k, e in enumerate(arr):
		if (e == 'x'):
			graph[j][k] = INF

def floydWarshall(graph): 
  
    """ dist[][] will be the output matrix that will finally 
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix 
    OR we can say that the initial values of shortest distances 
    are based on shortest paths considering no  
    intermediate vertices """
    dist = map(lambda i : map(lambda j : j , i) , graph) 
      
    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(V): 
  
        # pick all vertices as source one by one 
        for i in range(V): 
  
            # Pick all vertices as destination for the 
            # above picked source 
            for j in range(V): 
  
                # If vertex k is on the shortest path from  
                # i to j, then update the value of dist[i][j] 
                dist[i][j] = min(dist[i][j] , 
                                  dist[i][k]+ dist[k][j] 
                                ) 
    printSolution(dist) 
  
  
# A utility function to print the solution 
def printSolution(dist): 
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print "%7s" %("INF"), 
            else: 
                print "%7d\t" %(dist[i][j]), 
            if j == V-1: 
                print ""

def trimMatrix(adjMatrix, adjText)		
	editedMatrix = adjMatrix
	for loc in locations:
		if (adjText[loc].count('x') >= numloc - 2):
			del(editedMatrix[loc]) #delete row
			for adjcs in editedMatrix.values():
				del(adjcs[loc]) # delete column
	return editedMatrix



def ILPMatrix(editedMatrix):



print("Nested dictionary 1-") 
print(Dict) 

class Graph: 
      
    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 
  
    def DFSUtil(self, temp, v, visited): 
  
        # Mark the current vertex as visited 
        visited[v] = True
  
        # Store the vertex to list 
        temp.append(v) 
  
        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 
                  
                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 
  
    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 
  
    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc


class Node:
	def __init__(self, name, isHome):
		self.name = name
		self.isHome = False

	def __repr__(self):
		return repr(self.name)