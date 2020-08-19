switchthing = {
      56:[7,8],63:[7,9], 70:[7,10], 112:[7,16] , 301:[7,43], 72:[9,8], 80:[10,8], 128:[16,8], 344:[43,8], 90:[9,10], 144:[16,9], 387:[9,43], 160:[10,16], 430:[43,10], 688:[16,43]
  }


print("0 1", flush = True)
query1 = int(input())
print("1 2", flush = True)
query2 = int(input())
print("3 4", flush= True)
query3 = int(input())
print("4 5", flush= True)
query4 = int(input())
intersection= list(set(switchthing.get(query1))&set(switchthing.get(query2)))
intersection.insert(0,query1//intersection[0])
intersection.insert(2,query2//intersection[1])
intersection2= list(set(switchthing.get(query3))&set(switchthing.get(query4)))
intersection.insert(3,query3//intersection2[0])
intersection.insert(5,query4//intersection2[0])
intersection.insert(4,intersection2[0])
print(intersection)