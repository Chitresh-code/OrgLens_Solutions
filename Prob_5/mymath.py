def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    
    return result