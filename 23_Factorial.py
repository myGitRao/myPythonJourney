# Factorial by 2 approaches
# Iterative

def factorial_iterative(n):
    fact = 1
    for i in range(1, n):
        fact = fact * (i + 1)
    return fact


# Recursive
def factorial_recursive(n) :
    if n == 1:
        return 1
    else :
        fact = n * factorial_recursive(n - 1)
        return fact


# main body of the function
number = int(input("Enter the number whose factorial needs to calculated : "))
print("Now will execute the iterative factorial function")
print(factorial_iterative(number))
print("Now will execute the recursive factorial function")
print(factorial_recursive(number))
