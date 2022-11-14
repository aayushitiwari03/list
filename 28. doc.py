a=[1, 1, 2, 3, 4, 5, 1, 2]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)



a=[5,6,7,8,9,10,7,5]
i=0
b=[]
while i <len(a):
    if a[i]!=7 and a[i]!=5:
        b.append(a[i])
    i=i+1
print(b)