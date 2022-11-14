a=[-4,-3,-2,-1,0,1,2,3,4,5]
i=0
b=[]
while i<len(a):
    if a[i]<=0:
        b.append(a[i])
    i=i+1
print(b)


a=[-4,-3,-2,-1,0,1,2,3,4,5]
i=0
b=[]
c=[]
while i<len(a):
    if a[i]<=0:
        b.append(a[i])
    if a[i]>=0:
        c.append(a[i])
    i=i+1
print(b)