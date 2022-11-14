a=[1042,1100,1305,1105]
i=0
while i<len(a):
    sum=0
    b=str(a[i])
    j=0
    d=" "
    while j<len(b):
        if (b[j])!=str(1):
            d=d+(b[j])
            sum=sum+(int(b[j]))
        j+=1
    print([sum],end=" ")
    i+=1
