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


    def test_even(self):
        self.assertEqual(hexathon.even('aBc'), '0aBc')


    def test_uniform(self):
        self.assertEqual(hexathon.uniform('aBc'), '0abc')


    def test_unpad(self):
        self.assertEqual(hexathon.unpad('000abc'), '0abc')


    def test_compact(self):
        self.assertEqual(hexathon.compact('000abc'), 'abc')


if __name__ == '__main__':
    unittest.main()
