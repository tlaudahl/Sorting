# 1. A recursive algorithm must have a base case
# 2. A recursive algorithm must change its state and move toward the base case
# 3. A recursive algorithm must call itself, recursively

# Print every number, starting at number, until you reach 0
# def recurse(number):
#     if number <= 0:
#         return
#     print(number)
#     number -= 1
#     recurse(number) 
#     recurse(number) #2^n-1

# recurse(10)

# Fibonacci Sequence [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Return the Nth Fibonacci number

def fibonacci(n):
    if n < 0:
        raise ValueError("Can't have a negative number in the fibonacci sequence")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # return (n - 1) + (n - 2)
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(40))