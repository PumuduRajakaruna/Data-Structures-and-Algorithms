# In this code I used dictionary as a cache memory
# I memorize all fibonacci values after they calculate
# And they can be used in all over the code after that

cache = {}


def fibonacci(n):
    # if the value in the cache return it
    if n in cache:
        return cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    # cache the value and return it
    cache[n] = value
    return value


for i in range(1, 1001):
    print(i, " : ", fibonacci(i))
