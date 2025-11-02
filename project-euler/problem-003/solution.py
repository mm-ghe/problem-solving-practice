from math import sqrt

def is_prime(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False
    return True

def prime_factors(n):
    primes_list = []
    for j in range(2, int(sqrt(n))):
        if n % j == 0:
            if is_prime(j):
                primes_list.append(j)
            if is_prime(n//j):
                primes_list.append(n//j)
    print(max(primes_list))
    
print(prime_factors(600851475143))