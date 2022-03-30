#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
import sys, os

def read_file(file_name:str)->str:
    with open(file_name,"rb") as fd:
        file_content = fd.read()
    return file_content


def main():
    if len(sys.argv) != 2:
        print("[!] Usage: {} <pem file>".format(sys.argv[0]))
        sys.exit(-1)
    pem_file = sys.argv[1]
    if not os.path.exists(pem_file):
        print("[-] File {} doesn't exist".format(pem_file))
        sys.exit(-1)
    file_name,pem_file_extension = os.path.splitext(pem_file)
    print(pem_file_extension)
    if pem_file_extension != ".pem":
        print("[-] Not a PEM file")
        sys.exit(-1)
    key_encoded = read_file(pem_file)
    secret_key = RSA.importKey(key_encoded)
    print(secret_key.d)

if __name__ == "__main__":
    main()
