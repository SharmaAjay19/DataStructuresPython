class BST:
	def __init__(self, value):
		if type(value) not in [int, float]:
			raise Exception("Please provide correct data type")
		self.val = value
		self.left = None
		self.right = None
	def insert(self, value):
		if type(value) not in [int, float]:
			raise Exception("Please provide correct data type")
		if value <= self.val:
			if self.left:
				self.left.insert(value)
			else:
				self.left = BST(value)
		else:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BST(value)
	def search(self, value):
		if type(value) not in [int, float]:
			raise Exception("Please provide correct data type")
		if self.val == value:
			return True
		elif self.val < value:
			if self.right:
				return self.right.search(value)
			else:
				return False
		else:
			if self.left:
				return self.left.search(value)
			else:
				return False
	def inorder(self):
		result = []
		if self.left:
			result += self.left.inorder()
		result += [self.val]
		if self.right:
			result += self.right.inorder()
		return result
	def preorder(self):
		result = [self.val]
		if self.left:
			result += self.left.preorder()
		if self.right:
			result += self.right.preorder()
		return result
	def postorder(self):
		result = []
		if self.left:
			result += self.left.postorder()
		if self.right:
			result += self.right.postorder()
		result += [self.val]
		return result

tree = BST(20)
tree.insert(10)
tree.insert(25)
tree.insert(300)
tree.insert(22)
tree.insert(5)
tree.insert(-10)
tree.insert(12)
tree.insert(8)
print("SEARCH 10", tree.search(10))
print("SEARCH 29", tree.search(29))
print("INORDER", tree.inorder())
print("PREORDER", tree.preorder())
print("POSTORDER", tree.postorder())