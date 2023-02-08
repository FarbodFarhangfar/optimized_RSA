import unittest
from RSA.utils.extended_euclidean import *


class UtilsTest(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(5, 20), 5)
        self.assertEqual(gcd(5, 11), 1)
        self.assertNotEqual(gcd(5, 11), 3)

    def test_lcm(self):
        self.assertEqual(lcm(330, 75), 1650)
        self.assertEqual(lcm(450, 225), 450)
        self.assertNotEqual(lcm(450, 225), 500)




if __name__ == "__main__":
    unittest.main()
