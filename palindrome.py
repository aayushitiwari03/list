
name=[ 'n', 'i', 't', 'i', 'n' ]
b=name[::-1]   
if name==b:
    print(" haan ! palindrom  hain ")
else:
    print(" nahi palindrom nahin hain ")

name=[ 'n', 'i', 't', 'i', 'n' ]
i=len(name)
c=[]
while i>0:
    c.append(name[i-1])
    i-=1
if c==name:
    print("palindrom")
else:
    print("not palindrom")

name=[1,2,1]
i=len(name)
c=[]
while i>0:
    c.append(name[i-1])
    i-=1
if c==name:
    print("palindrom")
else:
    print("not palindrom")

a=[1,2,1]
b=len(a)
i=b-1
c=""
d=[]
while i>=0:
    c=(str(a[i]))
    d.append(int(c))
    i-=1
if a==d:
    print("oky")
else:
    print("not oky")