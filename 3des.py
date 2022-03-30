from Crypto.Cipher import DES3
import binascii

key = binascii.unhexlify('FFEEDDCCBBAA9988776655BBFFEEDDCCBBAA9988776655BB')
IV = binascii.unhexlify('0123456789ABCDEF')
encryptor = DES3.new(key, DES3.MODE_CBC, IV=IV)
text = binascii.unhexlify('0123456789ABCDEFFEDCBA98765432100123456789ABCDEFFEDCBA98765432100123456789ABCDEFFEDCBA98765432100123456789ABCDEFFEDCBA9876543210')
plaintext = encryptor.encrypt(text)
print(binascii.hexlify(plaintext).upper())
