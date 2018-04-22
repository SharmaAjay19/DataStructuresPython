class Heap:
	def __init__(self, heaptype, capacity):
		if heaptype.lower()=="min":
			self.heapType = "min"
		elif heaptype.lower()=="max":
			self.heapType = "max"
		else:
			raise Exception("Please specify a heap type")
		self.__head = [0]*capacity
		self.__capacity = capacity
		self.__heapSize = 0
	def parent(self, i):
		return int((i-1)/2)
	def left(self, i):
		return (2*i + 1)
	def right(self, i):
		return (2*i + 2)
	def getRoot(self):
		return self.__head[0]
	def insertKey(self, key):
		if self.__heapSize == self.__capacity:
			print("Heap overflow!")
			return
		self.__heapSize += 1
		ind = self.__heapSize - 1
		self.__head[ind] = key;
		while (ind>0) and ((self.__head[self.parent(ind)]>self.__head[ind]) if self.heapType=="min" else (self.__head[self.parent(ind)]<=self.__head[ind])):
			self.__head[ind], self.__head[self.parent(ind)] = self.__head[self.parent(ind)], self.__head[ind]
			ind = self.parent(ind)
	def changeKey(self, ind, new_val):
		self.__head[ind] = new_val
		while (ind>0) and ((self.__head[self.parent(ind)]>self.__head[ind]) if self.heapType=="min" else (self.__head[self.parent(ind)]<=self.__head[ind])):
			self.__head[ind], self.__head[self.parent(ind)] = self.__head[self.parent(ind)], self.__head[ind]
			ind = self.parent(ind)
	def extractRoot(self):
		if self.__heapSize<=0:
			return float("inf")
		if self.__heapSize == 1:
			self.__heapSize += -1
			return self.__head[0];
		root = self.__head[0]
		self.__head[0] = self.__head[self.__heapSize-1]
		self.__heapSize += -1
		self.Heapify(0)
		return root
	def deleteKey(self, keyIndex):
		if self.heapType=="min":
			self.changeKey(keyIndex, float("-inf"))
		else:
			self.changeKey(keyIndex, float("inf"))
		self.extractRoot()
	def Heapify(self, ind):
		l = self.left(ind)
		r = self.right(ind)
		if self.heapType=="min":
			smallest = ind
			if (l < self.__heapSize) and (self.__head[l] < self.__head[ind]):
				smallest = l
			if (r < self.__heapSize) and (self.__head[r] < self.__head[smallest]):
				smallest = r
			if smallest != ind:
				self.__head[ind], self.__head[smallest] = self.__head[smallest], self.__head[ind]
				self.Heapify(smallest)
		else:
			largest = ind
			if (l < self.__heapSize) and (self.__head[l] > self.__head[ind]):
				largest = l
			if (r < self.__heapSize) and (self.__head[r] > self.__head[largest]):
				largest = r
			if largest != ind:
				self.__head[ind], self.__head[largest] = self.__head[largest], self.__head[ind]
				self.Heapify(largest)
	def printHeap(self):
		print(self.__head[:self.__heapSize])

heap = Heap("max", 11)
heap.insertKey(3)
heap.insertKey(2)
heap.printHeap()
heap.deleteKey(1)
heap.printHeap()
heap.insertKey(15)
heap.insertKey(5)
heap.insertKey(4)
heap.insertKey(45)
heap.printHeap()
print(heap.extractRoot())
print(heap.getRoot())
heap.changeKey(2, 1)
print(heap.getRoot())
heap.printHeap()

'''
MIN
[2, 3]
[2]
[2, 4, 5, 15, 45]
2
4
1
[1, 15, 4, 45]'''

'''
MAX
[3, 2]
[3]
[45, 15, 5, 3, 4]
45
15
15
[15, 4, 1, 3]'''