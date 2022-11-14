
a=["shivani","rupa","shaina","samiksha","pooja"]
i=0
c=0
d=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if (a[i][j])=="s":
            c+=1
        if (a[i][j])=="r":
            d+=1  
        j+=1
    i+=1
print("in list a 's' is",c,"time")
print("in list a 'r' is",d,"time")