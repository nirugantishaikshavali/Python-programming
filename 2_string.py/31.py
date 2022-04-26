# # l="the hello how are you"
# # l=l.split(" ")
# # p=" ".join(reversed(l))
# # print(p)

# s="the quick brown fox jumps over the lazy dog"
# p="aeiou"
# l="".join(i for i in s if i not in p)
# print(l)

import collections
l=collections.defaultdict(int)
p="the quick brown fox jumps over the lazy dog"
for i in p:
    l[i]+=1
for i in sorted(l,key=l.get,reverse=True):
    if l[i]>1:
        print("%s %d"%(i,l[i]))