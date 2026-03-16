import time
import random
from src.generator import prime1, prime2, sieve

number = random.randint(10000, 100000)
while not prime1(number):
    number = random.randint(10000, 100000)

start_time = time.time()
print(f"Is {number} prime? (Square method): {prime1(number)}")
print(f"Time taken: {time.time() - start_time:.6f} seconds\n")
start_time = time.time()
print(f"Is {number} prime? (Naive method): {prime2(number)}")
print(f"Time taken: {time.time() - start_time:.6f} seconds\n")
start_time = time.time()
print(f"Prime numbers up to 100: {sieve(100)}")
print(f"Time taken: {time.time() - start_time:.6f} seconds\n")