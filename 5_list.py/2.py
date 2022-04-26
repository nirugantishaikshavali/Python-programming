l=[[2,3,4],[5,67,34],[65,35,7]]
p=[9,4,6]
# m=[]
# for i in range(len(p)):
    # m.append([])
m=[[] for i in range(len(p))]
for i in range(len(p)):
    m[i].append(p[i])

r=[x+y for x,y in zip(l,m)]
print(r)