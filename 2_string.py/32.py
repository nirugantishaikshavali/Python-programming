# from re import T


# def non_repeating(str1):
#     l={}
#     for i in str1:
#         if i in l:
#             l[i]+=1
#         else:
#             l[i]=1
#     for i in l:
#         if l[i]==1:
#             return i
#     return None
# str1="abcabcdef"
# print(non_repeating(str1))

# l="wdwfeqc.      com"
# p=[i for i in l if i!=" "]
# sp=len(l)-len(p)
# r=" "*sp+"".join(p)
# print(r)

# l="l&t give the good oppurtinity for every fresher"
# l=r=l.title()
# r=""
# for i in l.split(" "):
#     r+=i[:-1]+i[-1].upper()+" "
# print(r)


l="123abcdf45"
s=0
for i in l:
    if i.isdigit()==True:
        z=int(i)
        s+=z
print(s)