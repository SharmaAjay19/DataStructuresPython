#Undirected Graph
from Queue import Queue
class Graph:
	def __init__(self, size):
		self.size = size
		self.adjacencyList = [[] for i in range(size)]
	def addEdge(self, u, v):
		self.adjacencyList[u].append(v)
		self.adjacencyList[v].append(u)
	def DFSRecursive(self, vertex, visitedStatus):
		visitedStatus[vertex] = True
		print(vertex)
		for v in self.adjacencyList[vertex]:
			if visitedStatus[v] is False:
				self.DFSRecursive(v, visitedStatus)
	def DFS(self, vertex):
		print("DFS traversal of this graph starting from %d is:"%vertex)
		visitedStatus = [False for i in range(self.size)]
		self.DFSRecursive(vertex, visitedStatus)
	def BFS(self, vertex):
		print("BFS traversal of this graph starting from %d is:"%vertex)
		visitedStatus = [False for i in range(self.size)]
		traversalQueue = Queue(self.size)
		traversalQueue.enqueue(vertex)
		visitedStatus[vertex] = True
		while traversalQueue.isEmpty() is False:
			element = traversalQueue.dequeue()
			print(element)
			for v in self.adjacencyList[element]:
				if visitedStatus[v] is False:
					traversalQueue.enqueue(v)
					visitedStatus[v] = True
		
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
print(g.adjacencyList)
g.DFS(2)
g.BFS(2)'''