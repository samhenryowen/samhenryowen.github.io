from pythonds.basic import Stack

def infixEval(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    infixexpr = list(infixexpr)
    tokenList = []
    
    for token in infixexpr:
        if token != ' ':
            tokenList.append(token)
            tokenList.append(' ')
        else:
            continue
               
    tokenList = ''.join(tokenList).split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    postfixExpr = " ".join(postfixList)
    
    solution = postfixEval(postfixExpr)
    return postfixExpr, solution

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == '//':
        return op1 // op2
    elif op == "+":
        return op1 + op2
    elif op =="**":
        return op1 ** op2
    else:
        return op1 - op2
        

print(infixEval("(1 + 1) * 2"))