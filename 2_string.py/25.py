n="ab.c"
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
u=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
encr=[]
m=[]
decr=[]
for i in n:
    if i in l:
        index=(l.index(i)+2)%26
        encr.append(index)
        p=l[index]
        decr.append(p)
    else:
        decr.append(i)
print("".join(decr))
        
