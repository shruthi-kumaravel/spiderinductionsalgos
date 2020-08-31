def isprime(n): 
     
    for i in range(2, n): 
        if n % i == 0: 
            return False
  
    return True
n = int(input())
sum = 0
count = 0
for i in range(2,n+1):
  if isprime(i) == True:
    count = count + 1
print(count*(count+1)//2)
