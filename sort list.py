a=[45,78,1,90,67]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)





