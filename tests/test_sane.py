# standard imports
import unittest
import logging

# external imports
import hexathon

#logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger()


class TestSane(unittest.TestCase):

    def setUp(self):
        self.v_invalid = 'foo'
        self.v_empty = ''
        self.v_zero_pad = '00'
        self.v_zero = '0'
        self.v_value_pad = '0BA4'
        self.v_value = 'BA4'
        self.v_value_zerox_pad = '0x0BA4'
        self.v_value_zerox = '0xBA4'
        self.v_value_pad_long = '00BA4'
        self.v_value_pad_long_even = '000BA4'
        self.expect = {
            'invalid': ValueError,
            'empty': ValueError,
            'zero_pad': None,
            'zero': None,
            'value_pad': None,
            'value': None,
            'value_zerox_pad': None,
            'value_zerox': None,
            'value_pad_long': None,
            'value_pad_long_even': None,
                }


    def __check(self, m, **kwargs):
        for k in self.expect.keys():
            v = getattr(self, 'v_' + k)
            logg.debug('trying k {} v {} kwargs {} expect {}'.format(k, v, kwargs, self.expect[k]))
            if self.expect[k] == None:
                m(v, **kwargs)
            else:
                try:
                    if issubclass(self.expect[k], BaseException):
                        with self.assertRaises(self.expect[k]):
                            m(v, **kwargs)
                except TypeError:
                    r = m(v, **kwargs)
                    self.assertEqual(r, self.expect[k])


    def test_valid(self):
        self.expect['zero'] = ValueError
        self.expect['value'] = ValueError
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad_long'] = ValueError
        self.__check(hexathon.valid) 


    def test_valid_compact(self):
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.__check(hexathon.valid, allow_compact=True)



    def test_even(self):
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.__check(hexathon.even)


    def test_even_empty(self):
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['empty'] = None
        self.__check(hexathon.even, allow_empty=True)


    def test_even_compact(self):
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.__check(hexathon.even, allow_compact=True)


    def test_even_compact_empty(self):
        self.expect['empty'] = ''
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.__check(hexathon.even, allow_empty=True, allow_compact=True)


    def test_uniform(self):
        self.expect['value'] = '0ba4'
        self.expect['value_pad'] = '0ba4'
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.__check(hexathon.uniform)


    def test_strip_0x(self):
        self.expect['zero'] = '00'
        self.expect['zero_pad'] = '00'
        self.expect['value'] = '0BA4'
        self.expect['value_pad'] = '0BA4'
        self.expect['value_zerox'] = '0BA4'
        self.__check(hexathon.strip_0x)


    def test_strip_0x_compact(self):
        self.expect['zero'] = '0'
        self.expect['zero_pad'] = '0'
        self.expect['value'] = 'BA4'
        self.expect['value_pad'] = 'BA4'
        self.expect['value_zerox'] = 'BA4'
        self.__check(hexathon.strip_0x, compact_value=True)


    def test_strip_0x_empty(self):
        self.expect['empty'] = ''
        self.expect['zero'] = '00'
        self.expect['zero_pad'] = '00'
        self.expect['value'] = '0BA4'
        self.expect['value_pad'] = '0BA4'
        self.expect['value_zerox'] = '0BA4'
        self.__check(hexathon.strip_0x, allow_empty=True)


    def test_strip_0x_compact_empty(self):
        self.expect['empty'] = ''
        self.expect['zero'] = '0'
        self.expect['zero_pad'] = '0'
        self.expect['value'] = 'BA4'
        self.expect['value_pad'] = 'BA4'
        self.expect['value_zerox'] = 'BA4'
        self.expect['value_pad_long'] = 'BA4'
        self.expect['value_pad_long_even'] = 'BA4'
        self.__check(hexathon.strip_0x, allow_empty=True, compact_value=True)


    def test_add_0x(self):
        self.expect['value'] = '0x0BA4'
        self.expect['zero'] = '0x00'
        self.expect['zero_pad'] = '0x00'
        self.expect['value_pad'] = '0x0BA4'
        self.expect['value_zerox'] = '0x0BA4'
        self.expect['value_pad_long'] = '0x000BA4'
        self.expect['value_pad_long_even'] = '0x000BA4'
        self.__check(hexathon.add_0x)


    def test_add_0x_compact(self):
        self.expect['value'] = '0xBA4'
        self.expect['zero'] = '0x0'
        self.expect['zero_pad'] = '0x0'
        self.expect['value_pad'] = '0xBA4'
        self.expect['value_zerox'] = '0xBA4'
        self.expect['value_pad_long'] = '0xBA4'
        self.expect['value_pad_long_even'] = '0xBA4'
        self.__check(hexathon.add_0x, compact_value=True)


    def test_add_0x_empty(self):
        self.expect['empty'] = '0x'
        self.expect['value'] = '0x0BA4'
        self.expect['value_pad'] = '0x0BA4'
        self.expect['value_zerox'] = '0x0BA4'
        self.expect['value_pad_long'] = '0x000BA4'
        self.expect['value_pad_long_even'] = '0x000BA4'
        self.__check(hexathon.add_0x, allow_empty=True)


    def test_add_0x_compact_empty(self):
        self.expect['empty'] = '0x'
        self.expect['value'] = '0xBA4'
        self.expect['zero'] = '0x0'
        self.expect['zero_pad'] = '0x0'
        self.expect['value_pad'] = '0xBA4'
        self.expect['value_zerox'] = '0xBA4'
        self.expect['value_pad_long'] = '0xBA4'
        self.expect['value_pad_long_even'] = '0xBA4'
        self.__check(hexathon.add_0x, allow_empty=True, compact_value=True)


    def test_compact(self):
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad'] = 'BA4'
        self.expect['zero_pad'] = '0'
        self.__check(hexathon.compact)


    def test_unpad(self):
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad'] = '0BA4'
        self.expect['value_pad_long'] = '0BA4'
        self.__check(hexathon.unpad)


    def test_pad_noop(self):
        self.expect['zero'] = ValueError
        self.expect['value'] = ValueError
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad'] = '0BA4'
        self.expect['value_pad_long'] = ValueError
        self.expect['value_pad_long_even'] = '000BA4'
        self.__check(hexathon.pad)


    def test_pad_noop_compact(self):
        self.expect['zero'] = '00'
        self.expect['value'] = '0BA4'
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad_long_even'] = '000BA4'
        self.__check(hexathon.pad, allow_compact=True)


    def test_pad_to_four_bytes(self):
        #self.expect['zero'] = '00000000'
        self.expect['zero'] = ValueError
        self.expect['value'] = ValueError
        self.expect['value_pad_long'] = ValueError
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad'] = '00000BA4'
        self.expect['value_pad_long_even'] = '00000BA4'
        self.__check(hexathon.pad, byte_length=4)


    def test_pad_to_four_bytes_compact(self):
        self.expect['zero'] = '00000000'
        self.expect['value'] = '00000BA4'
        self.expect['value_pad_long'] = '00000BA4'
        self.expect['value_zerox_pad'] = ValueError
        self.expect['value_zerox'] = ValueError
        self.expect['value_pad'] = '00000BA4'
        self.expect['value_pad_long_even'] = '00000BA4'
        self.__check(hexathon.pad, byte_length=4, allow_compact=True)


if __name__ == '__main__':
    unittest.main()
