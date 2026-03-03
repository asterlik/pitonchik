def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

ind = 0
for num in range(245690, 245757):
    if is_prime(num):
        ind += 1
        print(ind, num)