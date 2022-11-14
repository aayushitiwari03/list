a=['Red', 'Maroon', 'Yellow', 'Olive']
c=[]
for i in a:
    b=[]
    for j in i:
        b.append(j)
    c.append(b)
print(c)


a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
while i<len(a):
    j=0
    while j<len(a[i])+1:
        print(a[i][-j],end=" ")
        j=j+1
    i=i+1