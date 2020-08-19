count = 0
def symmetry(n,a): 
 global count
 if n%2 == 0:
  mid = int(n/2)
  half1 = a[0 : mid ]
  half2 = a[ mid : n]
  if half1 == half2 :
   count = count + 1
   symmetry(mid, a)
 
 return count

string = input()
length = int(input())
print(symmetry(length, string))