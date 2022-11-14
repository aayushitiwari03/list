a=['Python', 'list', 'exercises', 'practice', 'solution']
i=0
c=[]
while i<len(a):
    b=(a[i][::-1])
    c.append(b)
    i+=1
print(c)