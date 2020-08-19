 len = int(input())
 n=input()
 d= int(n, 2)
 a=d-1
 b=d+1
 if b != pow(2,len):

  print(bin(a)[2:], bin(b)[2:])
 else:
   print ("no solution")
