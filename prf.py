#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import hmac
import binascii

def _p_hash(secret, seed, output_length):
    result = bytearray()
    i = 1
    while len(result) < output_length:
        h = hmac.new(secret,b'', hashlib.sha256)
        h.update(_a(secret, hashlib.sha256, i, seed))
        h.update(seed)
        result.extend(h.digest())
        i += 1
    return bytes(result[:output_length])


def _a(secret, hash_algorithm, n, seed):
    if n == 0:
        return seed
    else:
        h = hmac.new(secret,b'', hash_algorithm)
        h.update(_a(secret, hash_algorithm, n - 1, seed))
        return h.digest()


def prf(secret, label, seed, output_length):
    return _p_hash(secret, bytes(label,'US-ASCII') + seed, output_length)



premastersecret = binascii.unhexlify('00020325f41d3ebaf8986da712c82bcd4d554bf0b54023c29b624de9ef9c2f931efc580f9afb081b12e107b1e805f2b4f5f0f1d00c2d0f62634670921c505867ff20f6a8335e98af8725385586b41feff205b4e05a010823f78b5f8f5c02439ce8f67a781d90cbe6bf1ae7f2bc40a49709a06c0e31499bf02969ca42d203e566bcc696de08fa0102a0fd2e2330b0964abb7c443020de1cad09bfd6381ffb94daafbb90c4ed91a0613ad1dc4b4703af84c1d63b1a876921c6d5869d61ccb98ed13ae6c09a13fc91e14922f301cf8bcf000303a6049d2f07d983faa91b8f4e7265ecb815a7cbabc1450cb72b3c74107717aa24ac42f25b6c6784767d0e3546c4f7')
label = 'master secret'
Clienthello_random = '60b420bb3851d9d47acb933dbe70399bf6c92da33af01d4fb770e98c'
Serverhello_random = '59b69f76fef19ea7ead095601096af8db0c9ea5de7a1d39d000e88ae'
seed = binascii.unhexlify(Clienthello_random+Serverhello_random)
length = 88
prfoutput  = prf(premastersecret,label,seed,length)
print(prfoutput.hex())
