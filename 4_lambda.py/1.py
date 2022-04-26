# l=(1,2,3,4,5,6,7)
# m=list(map(lambda x:x+x+x,l))
# print(m)

# l=[1,2,3]
# l2=[4,5,6]
# l3=[7,8,9]
# m=list(map(lambda x,y,z:x+y+z,l,l2,l3))
# print(m)

# l=["RED","BLUE","BLACK","WHITE","PINK"]
# m=list(map(list,l))
# print(m)

# n=[10,20,30,40,50,60,70,80,90,100]
# p=[1,2,3,4,5,6,7,8,9,10]

# m=list(map(pow,n,p))
# print(m)

# from math import sqrt
# l=[4,5,2,9]
# m=list(map(sqrt,l))
# print(m)
# def sq(n):
#     return n*n
# n=l=[4,5,2,9]
# m=list(map(sq,n))
# print(m)

# def change(s):
#     return str(s).upper(),str(s).lower()

# ch={"a","b","E","f","a","i","o","U","a"}
# m=list(map(change,ch))
# print(m)

# l=[6,5,3,9]
# p=[0,1,7,7]

# def num(l,p):
#     return l-p,l+p
# r=list(map(num,l,p))
# print(r)

# l=[1,2,3,4]
# l2=[0,1,2,3]
# p=list(map(str,l))
# t=tuple(map(str,l))
# print(p,t)


# s=[("as","13/06/2","35kg"),("bc","14/07/7","55kg"),("cg","25/12/2","78kg")]
# n=map(lambda x:x[0],s)
# d=map(lambda x:x[1],s)
# w=map(lambda x:int(x[2][:2]),s)
# print(list(n),list(d),list(w))


# import itertools
# n=10
# def fac(x=0,y=1):
#     yield x
#     while True:
#         yield y
#         x,y=y,x+y
# res=list(itertools.islice(fac(),n))
# print(res)
# s=lambda x:x*x
# print(list(map(s,res)))


# def sum1(n):
#     # n=[1,2,3,4,5,-15]
#     sum2=0
#     for i in n:
#         sum2+=i
#     return sum2    
# n=[1,2,3,4,5,-15]
# p=list(map(int,n))
# m=sum1(p)
# print(m)

# from array import array
# def plus(a):
#     n=len(a)
#     n1=n2=n3=0
#     for i in a:
#         if i>0:
#             n1+=1
#         elif i<=0:
#             n2+=1
#         else:
#             n3+=1
#     return round(n1/n2),round(n2/n2),round(n3/n3)
# a=array('i',[0,1,2,-1,-5,6,0,-3,-2,3,4])
# l=list(map(int,a))
# p=plus(l)
# print(p)

# from operator import eq
# def c(n1,n2):
#     r=sum(map(eq,n1,n2))
#     return r
# n1=[1,2,3,4,5,6,7,8]
# n2=[2,2,3,1,2,6,7,9]
# print(c(n1,n2))


def list1(mark):
    r=map(dict,zip(*[[(key,val) for val in values] for key,values in mark.items()]))
    return list(r)
    
mark={"s":[88,89,62,95],"l":[77,78,84,80]}
print(list1(mark))