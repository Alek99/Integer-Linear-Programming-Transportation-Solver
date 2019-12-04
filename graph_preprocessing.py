file = open(input, "r")

numloc = int(file.readline())
numhouse = int(file.readline())

locations = file.readline().split()

houses = file.readline().split()

startingVertex = file.readline()

adjMatrix = {}
editedMatrix = {}
adjText = {}
for loc in locations:
	adjMatrix[loc] = {} 
	adjRow = file.readline()
	adjText[loc] = adjRow
	for i, adjDistance in enumerate(adjRow.split()):
		if (adjDistance is not 'x'):
			adjDistance = float(adjDistance)
		adjMatrix[loc][locations[i]] = adjDistance

def trimMatrix(adjMatrix, adjText)		
	editedMatrix = adjMatrix
	for loc in locations:
		if (adjText[loc].count('x') >= numLoc - 2):
			del(editedMatrix[loc]) #delete row
			for adjcs in editedMatrix.values():
				del(adjcs[loc]) # delete column
	return editedMatrix


for array in adjMatrix:
	zip(lisLoc, array)



for ele in locations:
	loc2adj[ele]


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