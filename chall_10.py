from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
backend = default_backend()

def encrypt_block(msg, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(msg) + encryptor.finalize()

def decrypt_block(ctxt, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data =  decryptor.update(ctxt) + decryptor.finalize()
    return decrypted_data

msg = os.urandom(16)
key = os.urandom(16)
ctxt = encrypt_block(msg, key)
msg_2 = decrypt_block(ctxt, key)

print(msg == msg_2)