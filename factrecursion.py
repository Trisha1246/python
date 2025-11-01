n=int(input("enter n:"))
      
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of n is :",factorial(n))
     
