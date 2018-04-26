from Graph import Graph
def dijkstra(graph, source):
	shortestPathSet = []
	overallSet = [i for i in range(graph.size)]
	mindistances = [float("inf") for i in range(graph.size)]
	mindistances[source] = 0
	while len(shortestPathSet)<graph.size:
		minind = overallSet[0]
		minval = mindistances[overallSet[0]]
		for x in overallSet:
			if mindistances[x]<minval:
				minind = x
				minval = mindistances[x]
		shortestPathSet.append(minind)
		overallSet.remove(minind)
		for nbr, w in graph.adjacencyList[minind]:
			if mindistances[minind]+w < mindistances[nbr]:
				mindistances[nbr] = mindistances[minind] + w
	print(mindistances)

def dijkstraWithpath(graph, source):
	shortestPathSet = []
	shortestPathParent = [source for i in range(graph.size)]
	overallSet = [i for i in range(graph.size)]
	mindistances = [float("inf") for i in range(graph.size)]
	mindistances[source] = 0
	shortestPathParent[source] = -1
	while len(shortestPathSet)<graph.size:
		minind = overallSet[0]
		minval = mindistances[overallSet[0]]
		for x in overallSet:
			if mindistances[x]<minval:
				minind = x
				minval = mindistances[x]
		shortestPathSet.append(minind)
		overallSet.remove(minind)
		for nbr, w in graph.adjacencyList[minind]:
			if mindistances[minind]+w < mindistances[nbr]:
				mindistances[nbr] = mindistances[minind] + w
				shortestPathParent[nbr] = minind
	print(mindistances)
	shortestPaths = []
	for x in range(graph.size):
		par = shortestPathParent[x]
		pathlist = [x]
		while par != -1:
			pathlist .append(par)
			par = shortestPathParent[par]
		shortestPaths.append(list(reversed(pathlist)))
	for path in shortestPaths:
		print(path)

'''g = Graph(10)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(0, 4)
g.addEdge(1, 5)
g.addEdge(3, 6)
g.addEdge(4, 7)
g.addEdge(7, 8)
g.addEdge(5, 9)
g.addEdge(8, 9)'''

g = Graph(10)
g.addEdge(0, 2, 1)
g.addEdge(1, 2, 2)
g.addEdge(2, 3, 1)
g.addEdge(0, 4, 1)
g.addEdge(1, 5, 2)
g.addEdge(3, 6, 4)
g.addEdge(4, 7, 5)
g.addEdge(7, 8, 11)
g.addEdge(5, 9, 3)
g.addEdge(8, 9, 2)
dijkstraWithpath(g, 2)