class Queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.elements = []
		self.size = 0
	def enqueue(self, element):
		if self.size < self.capacity:
			self.elements.append(element)
			self.size += 1
		else:
			raise(Exception("Queue is Full"))
	def dequeue(self):
		x = self.elements[0]
		del self.elements[0]
		self.size -= 1
		return x
	def print_queue(self):
		print(self.elements)
	def isEmpty(self):
		if self.size==0:
			return True
		else:
			return False