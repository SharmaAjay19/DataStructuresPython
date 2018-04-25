class Queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.elements = []
		self.size = 0
	def enqueue(self, element):
		if self.size == self.capacity:
			raise(Exception("Queue is Full"))
		else:
			self.elements.append(element)
			self.size += 1
	def dequeue(self):
		x = self.elements[0]
		del self.elements[0]
		self.size -= 1
		return x
	def print_queue(self):
		print(self.elements)