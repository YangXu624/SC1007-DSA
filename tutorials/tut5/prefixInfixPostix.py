PRECEDENCE = {
    "*": 5, "/": 5, "%": 5,
    "+": 4, "-": 4,
    "<<": 3, ">>": 3,
    "&&": 2,
    "=": 1
}

def inToPost(tokens):
    """
    push operands directly to new expression stack, and operators onto temporary stack
    when encountering an operator of lower precedence, pop all operators of equal or higher precedence
    when encountering closed bracket, pop until its buddy is found
    finally empty the stack
    """
    stack = []
    new_expression = []
    for token in tokens:
        if token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                new_expression.append(stack.pop()) # pop until reach other bracket
            if stack:
                stack.pop() # throw away bracket
        elif token in PRECEDENCE:
            while stack and stack[-1] != "(" and PRECEDENCE[token] <= PRECEDENCE[stack[-1]]: # if incoming higher than top of stack
                new_expression.append(stack.pop()) # pop all that are necessary
            stack.append(token)
        else:
            new_expression.append(token) # for numbers

    while stack:
        new_expression.append(stack.pop())

    return new_expression


def preToIn(tokens):
    """
    read right to left since its in prefix, pushing operands to stack
    encountering operator, pop 2 operands to operate on
    push (in brackets) as new operand to operate on
    """
    stack = []
    for token in tokens[::-1]: # go right to left
        if token not in PRECEDENCE: # if token is operand
            stack.append(token)
        else: # if token is operator
            left_op = stack.pop()
            right_op = stack.pop()
            stack.append(f"( {left_op} {token} {right_op} )") # push as a new operand
    return stack


def postToPre(tokens):
    """
    read left to right, pushing all operands to a stack
    encountering operator, pop 2 operands for it to operate on
    finally push this onto the stack as an operand itself
    """
    stack = []
    for token in tokens:
        if token not in PRECEDENCE:
            stack.append(token) # push to stack if number
        else: # if token is operator, pop 2 operands
            right_op = stack.pop()
            left_op = stack.pop()
            stack.append(f"{token} {left_op} {right_op}") # push as new operand
    return stack

if __name__ == "__main__":
    expression = input("Enter the expression: ")
    tokens = expression.split()
    # new_expression = inToPost(tokens)
    # new_expression = preToIn(tokens)
    new_expression = postToPre(tokens)
    print(" ".join(new_expression))