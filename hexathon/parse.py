import re


__re_valid = '^[0-9a-fA-F]+$'
def valid(hx):
    l = len(hx)
    if l == 0 or l % 2 != 0:
        raise ValueError('invalid hex (invalid length {})'.format(l))
    if not re.match(__re_valid, hx):
        raise ValueError('invalid hex (non-hex character)')
    return hx


def even(hx, allow_empty=False):
    if len(hx) % 2 != 0:
        hx = '0' + hx
    if allow_empty and len(hx) == 0:
        return ''
    return valid(hx)


def uniform(hx):
    return even(hx).lower()


def strip_0x(hx, allow_empty=False):
    if len(hx) == 0 and not allow_empty:
        raise ValueError('invalid hex')
    elif len(hx) < 2:
        raise ValueError('invalid hex')
    if hx[:2] == '0x':
        hx = hx[2:]

    return even(hx, allow_empty)


def add_0x(hx, allow_empty=False):
    if len(hx) == 0 and not allow_empty:
        raise ValueError('invalid hex')
    if hx[:2] == '0x':
        hx = hx[2:]
    return '0x' + even(hx, allow_empty)


def unpad(hx):
    hx = strip_0x(hx)
    i = 0
    for i in range(len(hx)):
        if hx[i] != '0':
            break
    hx = hx[i:]
    return even(hx)


def pad(hx, byte_length):
    hx = strip_0x(hx)
    hx = hx.rjust(byte_length * 2, '0')
    return hx


def int_to_minbytes(v, byteorder='big'):
#    c = 0x100
#    i = 1
#    while c <= v:
#        i += 1
#        c = c << 8
    l = ((v.bit_length() - 1) >> 3) + 1
    return v.to_bytes(l, byteorder=byteorder)


def int_to_minhex(v):
    return int_to_minbytes(v).hex()
