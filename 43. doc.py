a=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
b=[]
n=4
while i<len(a):
    if i==n:
        b.append(20)
        n=n+4
    b.append(a[i])
    i=i+1
print(b)

    
a=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
i=0
b=[]
n=3
while i<len(a):
    if i==n:
        b.append("z")
        n=n+3
    b.append(a[i])
    i=i+1
print(b)