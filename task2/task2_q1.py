def howmany(expr):
    stack = [] 
    count = 0
    for char in expr: 
        if char in "<": 
  
            # Push the element in the stack  
            stack.append(char) 
            count = count + 1
        else: 
  
            # IF current character is not opening bracket, then it must be closing.   
            # stack cannot be empty  
            if not stack: 
                return count
            stack.pop() 
            count = count + 1
   # Check Empty Stack 
    if stack: 
        return count
    return count
  
  
# Driver Code 
num = int(input())
for i in range (num):
 expr = input()
 print (howmany(expr))