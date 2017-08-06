class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

if __name__ == '__main__':
	q = Queue()

	q.enqueue(12)
	q.enqueue(3)
	print('Is queue empty? ', q.isEmpty())
	fifo = q.dequeue()
	print('Value removed from queue: ', fifo)
	print('Size of queue', q.size())