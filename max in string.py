
a=["aa","aaa","aaaa"]
i=0
max=0
while i<len(a):
    if len(a[i])>max:
        max=len(a[i])
        c=a[i]
    i=i+1
print(max)