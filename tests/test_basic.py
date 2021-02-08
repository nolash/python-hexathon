import unittest

import hexathon


class HexTest(unittest.TestCase):

    def test_valid(self):
        with self.assertRaises(ValueError):
            hexathon.valid('0x')

        with self.assertRaises(ValueError):
            hexathon.valid('ag')

        with self.assertRaises(ValueError):
            hexathon.valid('abc')

        hexathon.valid('9876543210fedcba')


    def test_0x(self):
        self.assertEqual(hexathon.strip_0x('0xabcd'), 'abcd')
        self.assertEqual(hexathon.add_0x('abcd'), '0xabcd')


    def test_uniform(self):
        self.assertEqual(hexathon.uniform('aBc'), '0abc')



if __name__ == '__main__':
    unittest.main()
