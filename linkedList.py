# Node Class - Each element in Linked List is made of a Node
class Node:
	# Add data to the Node and initialize the next pointer as none
	def __init__(self, data):
		self.data = data
		self.next = None

# Linked List Class
class LinkedList:
	# Initialize head of the Linked List
	def __init__(self):
		self.head = None

	# Insert a node at the begining of the Linked List
	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# Insert after a given node
	def insertAfter(self, prev_node, data):
		if prev_node is None:
			print("Previous node is not a valid node in linked list.")
			return

		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	# Insert a node at the end of the linked list
	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while(last.next):
			last = last.next
		last.next = new_node

	def printList(self):
		temp = self.head

		while(temp):
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
	llist = LinkedList()

	print("Insert 6 at the end of the list")
	llist.append(6)

	print("List status:")
	llist.printList()

	print("Insert 7 at the beginning of the list")
	llist.push(7)

	print("List status:")
	llist.printList()

	print("Insert 1 at the beginning of the list")
	llist.push(1)

	print("List status:")
	llist.printList()

	print("Insert 8 after 7")
	llist.insertAfter(llist.head.next, 8)

	llist.printList()
