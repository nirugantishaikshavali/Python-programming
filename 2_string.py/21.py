s="PyThon"
n=0
for i in s[:4]:
    if i.upper()==i:
        n+=1
if n>=2:
    print(s.upper())
else:
    print(s)
        