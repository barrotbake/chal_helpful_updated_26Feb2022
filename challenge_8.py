#!/usr/bin/env python3
from binascii import unhexlify

with open('data_8.txt') as file:
    ciphertexts = [unhexlify(line.strip()) for line in file]

def repeated_blocks(ciphertext, blocksize=16):
    """ The blocksize is in bytes """
    if len(ciphertext) % blocksize != 0:
        raise Exception('The ciphertext length is not a multiple of the blocksize')
    else:
        num_blocks = len(ciphertext) // blocksize

    blocks = [ciphertext[i*blocksize:(i+1)*blocksize] for i in range(num_blocks)]

    if len(set(blocks)) != num_blocks:
        return True
    else:
        return False

hits = [ciphertext for ciphertext in ciphertexts if repeated_blocks(ciphertext)]
