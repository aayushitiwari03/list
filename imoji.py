


chr=input("enter the letter : ")
if (chr>='A' and chr<='Z') or (chr>='a' and chr<='z'):
    print()
    sc=(input("enter the  special chr : "))
    if sc=="&" or sc=="%":
        print()
        num=int(input("enter :"))
        if num>=0:
            print()
            pas=chr+sc+(str(num))
            if len(pas)==6:
                print("this is your password =",pas)
            else:
                print("invalid password")
        else:
            print("need to be any digit")
    else:
        print("need to be any special charecter")
else:
    print("need to be any alphabet")


money=int(input("enter : "))
or_test=input("enter yes or no :")
if money>500 or or_test=="yes":
    print(" ravi will be going to movie ")
else:
    print("he will not be going for movie  ")

a=int(input("enter : "))
b=int(input("enter : "))
c=int(input("enter : "))
d=int(input("enter : "))
e=int(input("enter : "))
total=a+b+c+d+e
average=total/5
if total>average:
    print(total,"is this total score and the average is ",average,"class is performing well")


