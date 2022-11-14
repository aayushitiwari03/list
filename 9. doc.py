
a=int(input("enter the number : "))
b=[]
max=0
secondmax=0
thirdmax=0
i=0
while i<a:
    d=int(input("enter : "))
    b.append(d)
    if b[i]>max:
        thirdmax=secondmax
        secondmax=max
        max=b[i]
    i=i+1
print("this is our list",b)
print("max is =",max)
print("secondmax is =",secondmax)
print("third max is =",thirdmax)

