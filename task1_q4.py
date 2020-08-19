string= input()
cont=input()
scnood=input()
li = list(string.split(" "))
contest = list(cont.split(" "))
scn = list(scnood.split(" "))
n = int(li[0])
x = int(li[2])
y = int(li[3])
net = 0
for i in range(n):
  if contest[i] == "1" and scn[i] == "1":
    net = net+x
  if contest[i] == "1" and scn[i] == "0":
    net= net-y
if net>0:
  print("promoted")
elif net< 0:
  print("demoted")
else:
  print ("no change")