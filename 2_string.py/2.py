str1="google.com"
p={}

for i in  str1:
    if i not in p.keys():
        p[i]=1
    else:
        p[i]+=1
print(p)