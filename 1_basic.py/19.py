def is1(l):
    if len(l)>2 and l[:2]=="is":
        return l
    return "is"+l
l=input()    
print(is1(l))
    