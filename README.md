Prime Number Generator

This python project provides functions to check and generate prime numbers using three methods:

- **prime1(n)** -> Square method
- **prime2(n)** -> Naive method
- **sieve(n)** -> (Sieve of Eratosthenes) Generates a list of prime numbers up to n

## Installation

1. Ensure that the version of Python is 3.x
2. Clone the project:
```bash
git clone <repo_link>

---

## Usage

```markdown

Python konsolunda:

```python
from src.generator import prime1, prime2, sieve


print(prime1(17))  # True
print(prime2(18))  # False
print(sieve(20))   # [2, 3, 5, 7, 11, 13, 17, 19]

## Testler

```markdown
Unittest has been used in this project. To run all tests:

```bash
python - m unittest discover -s tests

## Additional Information

---

- Negative numbers, non-integers or strings will raise **ValueError**.
- The code handles both normal and edge cases.
- It can compare the speed of each prime-checking method for performance testing.

---
