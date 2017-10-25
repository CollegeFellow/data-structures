class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# Prints level order traversal of a tree using queue
def printLevelOrder(root):
	if root is None:
		return
	
	q = []
	q.append(root)
	
	while(len(q) > 0):
		current = q[0]
		print(current.val, end=" ")
		q.pop(0)

		if current.left is not None:
			q.append(current.left)
		if current.right is not None:
			q.append(current.right)


if __name__ == '__main__':
	#Driver Program to test above function
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	 
	print("Level Order Traversal of binary tree is -")
	printLevelOrder(root)