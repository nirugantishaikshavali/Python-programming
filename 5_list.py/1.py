# # p=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# # l=max(len(i) for i in p)
# # k=max(p,key=lambda x:len(x))
# # print(l,k)


# # # l=[[2],[0],[1,3],[0,7],[9,11],[13,15,17]]
# # # m=sorted(l,key=lambda x:(len(x),x))
# # # print(m)
# # # l=[[1,2,3],[2,4,5],[1,1,1]]
# # # m=sorted(l,key=lambda x:(len(x),x))
# # # print(m)
# # # p=["pyhton","list","exercises","practice","solution"]
# # # n=8
# # # l=list(filter(lambda x:len(x)==n,p))
# # # print(l)
# # # l=[1,"abcd",3.12,1.2,4,'xyz',5,'pqr',7,-5,-12.22]
# # # # p=len(list(filter(lambda x:x=float,l)))
# # # p=list(map(lambda i:isinstance(i,float),l))
# # # # print(p)
# # # m=len([i for i in p if ])
# # # print(m)

# l=[3,4,5,8,0,3,8,5,0,3,1,5,2,3,4,2]
# p=dict(map(lambda x:(x,list(l).count(x)),l))
# print(p)
