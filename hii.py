def factorial(n):
    lf n==0:
       return 1
     else:
        return n * factorial(n-1)  
        
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}.)       
