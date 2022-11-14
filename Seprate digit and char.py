a=["4efs","6gh3","12ab"]
i=0
d=[]
alpha=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        if (a[i][j])>=str(0) and (a[i][j])<=str(9):
            d.append(int(a[i][j]))
        else:
            alpha.append(a[i][j])
        j+=1
    i+=1
print(d)
print(alpha)
