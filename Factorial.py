def factorial(n):
    # single line to find factorial
    if (n == 1 or n == 0) :
        return 1
    else :
        return n * factorial(n - 1)

# Driver Code
num = 3
print("Factorial of", num, "is", factorial(num))