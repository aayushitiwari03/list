a=[2,44,45,6,2,3,45,0,32,12,90,1]
i=0
b=[]
while i<len(a):
    n=a.count(a[i])
    if n==1:
        b.append(a[i])
    i+=1
print(b)


   