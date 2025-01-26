# According to Python best practices, we should import all necessary libraries at the beginning of a program
# In this challenge, you don't need to import any additional libraries.

def print_numbers(n):
    # A for loop can be used to iterate over a sequence (like a list or a string) or other iterable objects.
    # The range() function generates a sequence of numbers. If you call range(n), it generates a sequence of numbers from 0 to n-1. 
    # But as we need to print numbers starting from 1 to n, we will use range(1, n+1)

    # You can now create a for loop using range(1, n+1), in each iteration check if the number 
    # is a multiple of 3, 5 or both and print accordingly

    # On case where number is multiple of both 3 and 5, you have to print 'FizzBuzz'
    # and break the loop

    # Syntax for for loop: 
    # for iter_var in sequence:
    #     # code here

    # To check if a number x is a multiple of y, you can use the modulo operator (%)
    # If x % y == 0, then x is a multiple of y.

    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
            break
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

n = int(input())

print_numbers(n)
