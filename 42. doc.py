a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i=0
n=3
while i<len(a):
    b=a[n:]+a[:n]
    i=i+1
print(b)