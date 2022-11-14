a=[12, 67, 98, 34]
i=0
b=[]
while i<len(a):
    n=str(a[i])
    j=0
    sum=0
    while j<len(n):
        sum+=int(n[j])
        j=j+1
    b.append(sum)
    i=i+1
print(b)

a=[15, 81, 11, 234]
i=0
b=[]
while i<len(a):
    n=str(a[i])
    j=0
    sum=0
    while j<len(n):
        sum+=int(n[j])
        j=j+1
    b.append(sum)
    i=i+1
print(b)