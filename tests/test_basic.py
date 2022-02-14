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
        self.assertEqual(hexathon.strip_0x('0x000abcd'), '0000abcd')
        self.assertEqual(hexathon.add_0x('000abcd'), '0x0000abcd')
        self.assertEqual(hexathon.strip_0x('0x000abcd', compact_value=True), 'abcd')
        self.assertEqual(hexathon.add_0x('000abcd', compact_value=True), '0xabcd')


    def test_even(self):
        self.assertEqual(hexathon.even('aBc'), '0aBc')


    def test_uniform(self):
        self.assertEqual(hexathon.uniform('aBc'), '0abc')


    def test_unpad(self):
        self.assertEqual(hexathon.unpad('000abc'), '0abc')


    def test_compact(self):
        self.assertEqual(hexathon.compact('000abc'), 'abc')
        self.assertEqual(hexathon.compact('0x000abc'), 'abc')
        self.assertEqual(hexathon.compact('abc'), 'abc')
        self.assertEqual(hexathon.compact('0xabc'), 'abc')


if __name__ == '__main__':
    unittest.main()
