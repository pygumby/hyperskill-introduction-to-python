# Importing necessary function from math library
from math import ceil, factorial

# Defining factorial function to calculate factorial of ceil value of a float
def float_ceil_factorial(n):
    if n < 0:
        return -1
    return factorial(ceil(n))

# Taking input from user
n = float(input())

# Calling the function with the user input
output = float_ceil_factorial(n)

# Printing the output
print(output)
