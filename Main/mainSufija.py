from claseStack import Stack
def infixToPostfix (infixExpr):
    prec = {}
    prec['*']= 3
    prec['/']= 3
    prec['+']= 2
    prec['-']= 2
    prec['(']= 1
    operStack = Stack() #Pila en donde se agregan los operadores
    postfixList = [] #Lista de salida
    tokenList = infixExpr.split() #Se coloca el nombre de que viene en los parametros

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            operStack.push(token)
        elif token == ')':
            topToken = operStack.pop() #para sacar el ultimo elemento de la fila
            while topToken != '(':
                postfixList.append(topToken)
                topToken = operStack.pop()
            else:
            while (not operStack.is_empty() and (prec[operStack.peek()] >= prec[token])):
                postfixList.append (operStack.pop())

              # operStack.push(token)
    while not operStack.is_empty():
        postfixList.append(operStack.pop())

    return postfixList

espresion = 'A * B + C * D'
print ('expresion', expresion)
print (infixToPostfix(expresion))

                
            
    
    
