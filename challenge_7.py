#!/usr/bin/env python3
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64decode

backend = default_backend()

def decrypt_aes_128_ecb(ciphertext, key):
    """ AES in ECB mode """
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data =  decryptor.update(ciphertext) + decryptor.finalize()
    message = decrypted_data
    return message

with open("data_7.txt") as file:
    data = file.read()

print(decrypt_aes_128_ecb(ciphertext = b64decode(data), key=b"YELLOW SUBMARINE").decode())
