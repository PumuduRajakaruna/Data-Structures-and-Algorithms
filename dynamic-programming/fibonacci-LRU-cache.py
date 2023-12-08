from functools import lru_cache
# LRU = least recently used cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    # if n < 1:
    #     raise ValueError("n must be a positive integer")
    # if type(n) != int:
    #     raise TypeError("n must be an integer")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 1001):
    print(i, " : ", fibonacci(i))
