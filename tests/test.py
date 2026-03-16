import unittest
from src.generator import prime1, prime2, sieve

class TestPrimeMethods(unittest.TestCase):
    def test_prime1(self):
        self.assertTrue(prime1("2"))

if __name__ == '__main__':
    unittest.main()