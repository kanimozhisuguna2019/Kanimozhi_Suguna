# Factorial of a number using recursion

def recur_factorial(m):
   if m == 1:
       return m
   else:
       return m*recur_factorial(m-1)

num = 10

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
