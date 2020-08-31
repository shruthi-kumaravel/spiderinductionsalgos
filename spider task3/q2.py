n = int(input())
m = int(input())
strength=[]
answer = 0
for i in range(0,m):
  strength.append(int(input()))
strength.sort()
#if n one answer is sum f all bricks
if n == 1:
  for i in strength :
    answer= answer + i
if n == 2 :
  while len(strength)>2:
    #combine smollest two 
    temp = (strength[0]+strength[1])
    #seperate the rest
    strength = strength[2:]
    for i in strength:
      if temp <= i:
        #to make sure order is maintained 
        strength.insert(strength.index(i),temp)
        break
answer = strength[0]

print(answer)