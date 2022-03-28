from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from chall_9 import pkcs7_pad
from chall_10 import encrypt_block
backend = default_backend()
import random
import os

def encrypt_ecb(msg, key):
    padded_msg = pkcs7_pad(msg, block_size=16)
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(padded_msg) + encryptor.finalize()

def decrypt_ecb(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data =  decryptor.update(ctxt) + decryptor.finalize()
    return decrypted_data

for _ in range(5):
    length = random.randint(5,50)
    msg = os.urandom(length)
    key = os.urandom(16)
    iv = os.urandom(16)
    ctxt = encrypt_block(msg, iv, key)

def encryption_oracle(message):
    key = os.urandom(16)
    random_header = os.urandom(random.randint(5, 10))
    random_footer = os.urandom(random.randint(5, 10))
    to_encrypt = random_header + message + random_footer
    
    if mode == 'ECB':
        return encrypt_ecb(to_encrypt, key)
    iv = os.urandom(16)
    return encrypt_block(to_encrypt, iv, key)
    
    
for _ in range(10):
    mode = random.choice(['ECB', 'CBC'])
    message = b'A'*50
    ctxt = encryption_oracle(message, mode)