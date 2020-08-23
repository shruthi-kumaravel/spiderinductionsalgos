len = int (input())
arr = []
# creating array
for i in range(len):
  arr.append(i+1) 
num = int (input())
for i in range(num):
  quer = input()
  qu = list(quer.split(" "))
  # convert to tring
  for i in range (0,3):
    qu[i] = int(qu[i])
  for i in range(qu[0]-1, qu[1]):
    arr[i] = arr[i]+ qu[2]
print (max(arr))