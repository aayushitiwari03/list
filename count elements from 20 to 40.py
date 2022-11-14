n=[50,40,23,70,56,12,5,10,7]
lenght=len(n)
i=0
c=0
while i<lenght:
    num=n[i]
    if num>=20 and num<=40:
        c=c+1
    else:
        print("")
    i+=1
print("numbers between 20 and 40 is =",c)