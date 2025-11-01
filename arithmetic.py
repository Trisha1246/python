def cal(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=cal(100,50) 
print("the results are")
for i in t:
    print(i)
    
