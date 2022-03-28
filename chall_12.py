import base64
import imp
import os
from chall_10 import encrypt_block


DATA_TO_APPEND = base64.b64decode(
    "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
    "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
    "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
    "YnkK"
)

class ECB_Oracle:
    def __init__(self):
        self.key = os.urandom(16)

    def encrypt(self, msg):
        return encrypt_block(msg + DATA_TO_APPEND, self.key)

def block_size(oracle):
    current_ctxt = None
    for i in range(2, 20):
        previous_ctxt = current_ctxt or oracle.encrypt(b"A"*1)
        current_ctxt = oracle.encrypt(b"A"*i)
        if previous_ctxt[:4] == current_ctxt[:4]:
            return i-1

oracle = ECB_Oracle()
block_size = block_size(oracle)
assert block_size == 16

def payload_length(oracle):
    previous_length = len(oracle.encrypt(b''))
    for i in range(20):
        length = len(oracle.encrypt(b'X'*i))
        if length != previous_length:
            return previous_length - i

def recover_byte(oracle, known_plaintext, block_size):
    k = len(known_plaintext)
    padding_length = (-k-1) % block_size
    padding = b"A" * padding_length
    target_block_number = len(known_plaintext) // block_size
    target_slice = slice(target_block_number*block_size,(target_block_number+1)*block_size)
    target_block = oracle.encrypt(padding)[target_slice]

    for i in range(256):
        message = padding + known_plaintext + bytes([i])
        block = oracle.encrypt(message)[target_slice]
        if block == target_block:
            return bytes([i])

def byte_load(oracle, block_size):
    known_plaintext = b""

    payload_length = payload_length(oracle)
    for _ in range(payload_length):
        new_known_byte = recover_byte(oracle, known_plaintext, block_size)
        known_plaintext = known_plaintext + new_known_byte
    return known_plaintext

secret = byte_load(oracle, block_size)

print(secret.decode())