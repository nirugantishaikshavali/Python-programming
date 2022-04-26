def atleast(str1):
    if len(str1)==3:
        return str1+"ing"
    elif len(str1)>3 and str1[-3:]=="ing":
        return str1+"ly"
str1="string"
print(atleast(str1))