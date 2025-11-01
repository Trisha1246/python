a = int(input("enter the value :: "))
b = int(input("enter the value :: "))
c = int(input("enter the value :: "))
if(a>b and a>c):
    if(b>c):
        print(a,b,c)
    else:
        print(a,c,b)
elif(b>c and b>a):
    if(c>a):
        print(b,c,a)
    else:
        print(b,a,c)
elif(a>b):
    print(c,a,b)
else:
    print(c,b,a)
