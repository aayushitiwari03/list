a=[1,2,[3,4,[5],6,7,8]]
i=0
while i<len(a):
    if type(a[i])==(list):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                print(a[i][j])
            j+=1
    i+=1