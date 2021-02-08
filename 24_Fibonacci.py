# Calculating fibonacci series
# Series 0 1 1 2 3 5 8 13
# Iterative
def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        first = 0
        second = 1
        for i in range(1, n) :
            temp = first + second  #
            first = second
            second = temp
        return temp


# Recursive
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


number = int(input("Enter the number to find its fibonacci: "))
print(fibonacci_iterative(number))
print(fibonacci_recursive(number))
