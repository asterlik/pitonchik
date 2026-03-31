from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_gen(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

limit = 160
primes = prime_gen(limit)
print(next(primes))
print(next(primes))
total = reduce(lambda x, y: x + y, primes, 0)
print(total)