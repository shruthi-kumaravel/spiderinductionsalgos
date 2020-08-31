    n = input()
    sumofdig = 0
    count = 0 
    while (len(n) > 1): 
      
        sumofdig = 0
  
        # find sum of digits 
        for i in range(len(n)): 
            sumofdig = sumofdig + int(n[i]) 
  
        # converting t string for next iteration
        n = str(sumofdig) 
        count = count + 1
  
    print(count)