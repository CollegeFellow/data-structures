from sys import maxsize

# Create and return a new stack
def createStack():
	stack = []
	return stack

# Returns boolean if stack is empty or not
def isEmpty(stack):
	return (len(stack) == 0)

# Push an item to stack
def push(stack, item):
	stack.append(item)

def pop(stack):
	if(isEmpty(stack)):
		return str(-maxsize -1)		# Returns minus infinite
	return stack.pop()

def top(stack):
	return stack[(len(stack) - 1)]
		
if __name__ == "__main__":
	stk = createStack()

	print("Is the stack empty? ", str(isEmpty(stk)))

	push(stk, 1)
	print("Pushed 1 to the stack")
	
	push(stk, 2)
	print("Pushed 2 to the stack")
	
	push(stk, 3)
	print("Pushed 3 to the stack")
	
	print("Is the stack empty? ", str(isEmpty(stk)))

	print("Pop one item from the stack")
	pop(stk)

	print("Stack top: ", str(top(stk)))	
