# Define operator precedence globally 
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        self.top = self.top.next
        self.size -= 1

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data

def in2preS(expr):
    tokens = expr[::-1]
    for i in range(len(tokens)):
        if tokens[i] == "(":
            tokens[i] = ")"
        elif tokens[i] == ")":
            tokens[i] = "("

    s = Stack()
    expression = Stack()
    # shunting-yard algorithm
    for token in tokens:
        if token == "(":
            s.push(token)
        elif token == ")":
            while not s.isEmpty() and s.peek() != "(":
                expression.push(s.peek())
                s.pop()
            if not s.isEmpty():
                s.pop()  # discard '('
        elif token in PRECEDENCE: # catches operators
            while (not s.isEmpty() and s.peek() != "(" and (PRECEDENCE.get(s.peek(), 0) > PRECEDENCE[token] or (PRECEDENCE.get(s.peek(), 0) == PRECEDENCE[token] and token == '**'))):
                expression.push(s.peek()) # pop all with higher precedence
                s.pop()
            s.push(token)
        else:
            # add numbers directly to expression
            expression.push(token)

    while not s.isEmpty():
        expression.push(s.peek())
        s.pop()

    return expression

if __name__ == "__main__":
    infix = input("Enter infix expression: ")
    prefix = in2preS(list(infix.split(' ')))
    
    # Print the prefix expression
    result = ""
    while not prefix.isEmpty():
        result += prefix.peek()
        prefix.pop()
    
    print(f"Prefix expression: {result}")

"""
test cases
3 + 4 * 5
( 1 + 5 * 2 ** 2 + 2 ) + 7 ** 2 - 5 / 8 + 3 * 2 - ( 3 + 5 ** 2 )
"""