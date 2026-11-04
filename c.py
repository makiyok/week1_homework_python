

primes = []

for num in range(2, 41):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(num)

print(primes)

