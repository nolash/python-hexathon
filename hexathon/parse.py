import re


__re_valid = '^[0-9a-fA-F]+$'
def valid(hx):
    if len(hx) == 0 or len(hx) % 2 != 0:
        raise ValueError('invalid hex')
    if not re.match(__re_valid, hx):
        raise ValueError('invalid hex')
    return hx


def uniform(hx):
    if len(hx) % 2 != 0:
        hx = '0' + hx
    return valid(hx).lower()


def strip_0x(hx):
    if len(hx) < 2:
        raise ValueError('invalid hex')
    if hx[:2] == '0x':
        hx = hx[2:]
    return valid(hx)


def add_0x(hx):
    if len(hx) < 2:
        raise ValueError('invalid hex')
    if hx[:2] == '0x':
        hx = hx[2:]
    return '0x' + valid(hx)
