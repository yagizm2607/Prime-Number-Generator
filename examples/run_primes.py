from src.generator import prime1, prime2, sieve

import random

n1 = random.randint(2, 1000)
while not prime1(n1):
    n1 = random.randint(2, 1000)
n2 = random.randint(2, 1000)
while not prime2(n2):
    n2 = random.randint(2, 1000)




print("Random prime number with Square method", n1)
print("Random prime number with Naive method", n2)
print("Sieve of Eratosthenes prime up to 100\n", sieve(100))





