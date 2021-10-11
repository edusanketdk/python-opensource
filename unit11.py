import unittest

# Method assertIsInstance()
# UnitTestBy Hathaipach I.

class Empclass:
    Name = 'Maria'
    Birthday = '10-Dec-1997'
    Garden = 'Male'

class TestClass(unittest.TestCase):
    # test function to test whether obj is instance of class
    def test_positive(self):
        objectName = Empclass()
        # error message in case if test case got failed
        message = "An object is not instance of Empclass."
        self.assertIsInstance(objectName, Empclass, message)


if __name__ == '__main__':
    unittest.main()