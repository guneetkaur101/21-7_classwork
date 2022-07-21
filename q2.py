l1=[[4,5,3],[6,3,2],[6,9,1]]
res = []
for i in range (0,len(l1[0])):
    sum=0
    for j in range (0,len(l1)):
        sum=sum+l1[i][j]
    res.append(sum)
print( res)