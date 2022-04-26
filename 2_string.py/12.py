str1="the quick brown fox jumps over the lazy dog"
d={}
for i in str1.split(" "):
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)