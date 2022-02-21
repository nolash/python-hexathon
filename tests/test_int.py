# standard imports
import unittest

# local imports
import hexathon

class TestInt(unittest.TestCase):
    
    def test_1_bytes_min(self):

        v = 129
        r = hexathon.int_to_minbytes(v)
        self.assertEqual(r, b'\x81')

        v = 1025
        r = hexathon.int_to_minbytes(v)
        self.assertEqual(r, b'\x04\x01')

        v = 65536
        r = hexathon.int_to_minbytes(v)
        self.assertEqual(r, b'\x01\x00\x00')


    def test_2_hex_min(self):

        v = 129
        r = hexathon.int_to_minhex(v)
        self.assertEqual(r, '81')

        v = 1025
        r = hexathon.int_to_minhex(v)
        self.assertEqual(r, '0401')

        v = 65536
        r = hexathon.int_to_minhex(v)
        self.assertEqual(r, '010000')


    def test_to_int(self):

        v = '123'
        r = hexathon.to_int(v)
        self.assertEqual(r, 291)

        v = '0123'
        r = hexathon.to_int(v)
        self.assertEqual(r, 291)

        with self.assertRaises(ValueError):
            hexathon.to_int(v, need_prefix=True)

        r = hexathon.to_int(hexathon.add_0x(v), need_prefix=True)
        self.assertEqual(r, 291)

        with self.assertRaises(ValueError):
            hexathon.to_int('foo')


if __name__ == '__main__':
    unittest.main()
