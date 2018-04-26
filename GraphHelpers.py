from Graph import Graph
class GraphHelpers:
	def DFS(self, graph, visitedStatus, vertex, parent):
		visitedStatus[vertex] = True
		for v, w in graph.adjacencyList[vertex]:
			if visitedStatus[v]:
				if not (v==parent):
					return True
			else:
				return self.DFS(graph, visitedStatus, v, vertex)
		return False
	def detectCycle(self, graph, vertex):
		visitedStatus = [False for i in range(graph.size)]
		visitedStatus[vertex] = True
		for v, w in graph.adjacencyList[vertex]:
			if self.DFS(graph, visitedStatus, v, vertex):
				return True
		return False


g = Graph(10)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(0, 4)
g.addEdge(1, 5)
g.addEdge(3, 6)
g.addEdge(4, 7)
g.addEdge(7, 8)
g.addEdge(5, 9)
#g.addEdge(8, 9)
#print(g.adjacencyList)
print(GraphHelpers().detectCycle(g, 9))