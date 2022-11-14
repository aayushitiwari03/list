b=int(input("enter ther number : "))
a=[1,15,3,47,5,90,7,34,9]
i=0
d=1
while i<len(a):
    if i%2==0:
        c=d*b
        del(a[i])
        a.insert(i, c)
        d+=1
    i+=1
print(a)