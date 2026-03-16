import unittest
from src.generator import prime1, prime2, sieve

class TestPrimeMethods(unittest.TestCase):
    def test_prime1(self):
        self.assertTrue(prime1(2))
        self.assertTrue(prime1(3))
        self.assertFalse(prime1(4))
        self.assertTrue(prime1(5))
    def test_prime2(self):
        self.assertTrue(prime2(2))
        self.assertTrue(prime2(3))
        self.assertFalse(prime2(4))
        self.assertTrue(prime2(5))
    def test_sieve(self):
        self.assertEqual(sieve(10), [2, 3, 5, 7])
        self.assertEqual(sieve(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(sieve(1), [])
        self.assertEqual(sieve(2), [2])

    def test_prime_negative(self):
        with self.assertRaises(ValueError):
            prime1(-1)
        with self.assertRaises(ValueError):
            prime2(-1)
        with self.assertRaises(ValueError):
            sieve(-1)

    def test_prime_non_integer(self):
        with self.assertRaises(ValueError):
            prime1(2.5)
        with self.assertRaises(ValueError):
            prime2(2.5)
        with self.assertRaises(ValueError):
            sieve(2.5)
    
    def test_prime_string(self):
        with self.assertRaises(ValueError):
            prime1("string")
        with self.assertRaises(ValueError):
            prime2("string")
        with self.assertRaises(ValueError):
            sieve("string")

    

if __name__ == '__main__':
    unittest.main()