# Given a binary tree, print level order traversal in a way that nodes of all levels are printed in separate lines.
# 
# For eg. Given tree below
#           1
#       /     \
#      2       3
#    /   \       \
#   4     5       6
#        /  \     /
#       7    8   9
#
# ===============================
# Output for above tree should be
# 1
# 2 3
# 4 5 6
# 7 8 9
# ===============================

class Node:
	def __init__(self, val):
		self.left 	= None
		self.right 	= None
		self.val 	= val


def printLevelOrderLineByLine(root):
	if root is None:
		return

	q1 = []
	q2 = []
	q1.append(root)


	while(len(q1) > 0 or len(q2) > 0):
		while(len(q1) > 0):
			if q1[0].left is not None:
				q2.append(q1[0].left)
			if q1[0].right is not None:
				q2.append(q1[0].right)
			print(q1[0].val, end=" ")
			q1.pop(0)
		print()
		while(len(q2) > 0):
			if q2[0].left is not None:
				q1.append(q2[0].left)
			if q2[0].right is not None:
				q1.append(q2[0].right)
			print(q2[0].val, end=" ")
			q2.pop(0)
		print()

#Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Line by line Level Order Traversal of binary tree is -")
printLevelOrderLineByLine(root)