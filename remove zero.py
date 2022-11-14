
a=[1042,1100,1305,1105]
i=0
c=[]
while i<len(a):
    b=str(a[i])
    j=0
    d=" "
    while j<len(b):
        if (b[j])!=str(0):
            d=d+(b[j])
        j+=1
    c.append(int(d))
    i+=1
print(c)

