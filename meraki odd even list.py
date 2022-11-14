a=int(input("enter the number : "))
c=[]
i=0
e=[]
o=[]
while i<a:
    d=int(input("enter the number : "))
    c.append(d)
    if c[i]%2==0:
        e.append(c[i])
    else:
        o.append(c[i])
    i=i+1
print( "odd = ",o)
print("even = ",e)



