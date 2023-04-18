import unittest
from palindro import palindrome
from palindro import palindromeRecusivo

class TestPalindrome(unittest.TestCase):

    def test_palindrome_1 (self):

        result =palindrome ("neuquen")
        self.assertEqual (result,True)

class TestPalindromeRecursivo(unittest.TestCase):

    def test_palindrome_1 (self):

        result =palindromeRecusivo ("neuquen")
        self.assertEqual (result,True)

        

if __name__ == "__main__":
    unittest.main()        
