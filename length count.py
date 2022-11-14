i=0
a=[]
max=0
while i<5:
    b=input("enter : ")
    a.append(b)
    j=0
    while j<len(a[i]):
        if len(a[i])>max:
            c=(a[i])
            max=len(a[i])
        j+=1
    i+=1
print(a)
print("maximum len is",max,"and the name is",c)





