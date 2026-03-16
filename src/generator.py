import random
import math

# Square method
def prime1(n):
    """
    Check if n is prime.
    
    Returns True if n is prime, False otherwise.
    """
    if isinstance(n, str):
        raise ValueError("Input must be an integer, not a string.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if int(n) != n:
        raise ValueError("Input must be an integer.")
    if n > 2 and n % 2 == 0:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# Naive method
def prime2(n):
    """
    Check if n is prime.
    
    Returns True if n is prime, False otherwise.
    """
    if isinstance(n, str):
        raise ValueError("Input must be an integer, not a string.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if int(n) != n:
        raise ValueError("Input must be an integer.")
    return sum(1 for i in range(1, n+1) if n % i == 0) == 2

# Sieve of Eratosthenes
def sieve(n):
    """
    Generates prime numbers up to n.
    
    """
    if isinstance(n, str):
        raise ValueError("Input must be an integer, not a string.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if int(n) != n:
        raise ValueError("Input must be an integer.")
    list0 = [x for x in range(2, n+1)]
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [x for x in list0 if is_prime[x]]




    