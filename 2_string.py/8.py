# l=["php","exercise","backend"]
# lon=[]
# for i in l:
#     lon.append((len(i),i))
# lon.sort()
# print(lon[-1][-1])
l=[12,64,98,56,3,45,1144]
l1=l[0]
for i in l:
    if i>l1:
        l1=i
print(l1)