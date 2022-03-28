#!/usr/bin/env python3
from subprocess import check_output
from base64 import b64decode

def key_size():
  """ Create a list of possible key sizes within the range """
  start = 2
  end = 40
  return list(range(start, end + 1))

def convert(txt):
  """ Convert text consisting of ASCII characters to bytes """
  return bytearray.fromhex(txt.encode('utf-8').hex())

def match(byte_set_1, byte_set_2):
  """ XOR two sets of bytes with matching lengths """
  assert len(byte_set_1) == len(byte_set_2), 'Attempting to XOR bytes of varying lengths'
  return [byte_set_1[i] ^ byte_set_2[i] for i, x in enumerate(byte_set_1)]

def calc_hamming_dist(input_1, input_2):
  """ Compute the hamming distance between two inputs """
  xor_bytes = match(input_1, input_2)
  binary_bytes = [bin(i)[2:] for i in xor_bytes]
  binary_string = ''.join(binary_bytes)
  binary = list(map(int, list(binary_string)))
  count = sum(binary)
  return count
assert calc_hamming_dist(convert('this is a test'), convert('wokka wokka!!!')) == 37, 'Incorrect hamming distance calculation'

def split_chunks(iterable, chunk_size):
  """ Split an iterable into chunks of a specific size """
  chunks = [
    iterable[i:i + chunk_size]
    for i
    in range(0, len(iterable), chunk_size)
    if i < len(iterable) - chunk_size
  ]
  return chunks

def normalized_hamming_dist(txt, key_size):
  """ Calculate the normalized hamming distance for the two strings """
  assert key_size < len(txt) / 2, 'The text is too short to provide two blocks with this key size'
  byte_list = b64decode(txt)
  assert isinstance(byte_list, (bytes, bytearray)), 'The hamming distance must be calculated with raw bytes'
  chunks = split_chunks(byte_list, key_size)
  blocks = [
    byte_list[0:key_size],
    byte_list[key_size:key_size * 2]
  ]
  hamming_distances = [
    [calc_hamming_dist(block, chunk) for chunk in chunks]
    for block in blocks
  ][0]
  average = sum(hamming_distances) / len(hamming_distances)
  normalized_distance = average / key_size
  return normalized_distance

def smallest_hamming_dist(values):
  """ Find the key sizes that correspond to the smallest hamming distances in a list """
  sorted_values = sorted(values, key=lambda x: x.get('distance'))
  return sorted_values[0].get('key_size')

def remote():
  """ Retrieve the ciphertext from the cryptopals site """
  url = "https://cryptopals.com/static/challenge-data/6.txt"
  return check_output(['curl', '--silent', url]).decode('ascii')

def find_key_size(txt):
  """ Find the key size for a piece of encrypted text """
  normalized_hamming_distances = [
    {
      'key_size': key_size,
      'distance': normalized_hamming_dist(txt, key_size)
    }
    for key_size in key_size()
  ]
  keys = smallest_hamming_dist(normalized_hamming_distances)
  return keys

def transpose(text, size):
  """ Transpose the input text bytes by a specified size """
  byte_list = b64decode(text)
  chunks = split_chunks(byte_list, size)
  transposed = list(zip(*chunks))
  assert chunks[0][0] == transposed[0][0], 'matrix transposition failed'
  assert chunks[0][1] == transposed[1][0], 'matrix transposition failed'
  assert chunks[0][2] == transposed[2][0], 'matrix transposition failed'
  return transposed

def sinlge_xor(byte_list, key):
  """ XOR a set of bytes against a single key """
  return [b ^ key for b in byte_list]

def generate_ascii():
  """ Generate ASCII characters """
  return [chr(x) for x in range(128)]

def detect_key(strings):
  """ Detect a key given a set of input strings """
  common = list('etaoin shrdlu')
  counts = [
    sum([string.count(character) for character in common])
    for string in strings
  ]
  maximum = max(counts)
  index = counts.index(maximum)
  return chr(index)

def find_xor_key(byte_list):
  """ Statistically determine the single most likely key given a set of XOR encrypted input bytes """
  xor_bytes = [sinlge_xor(byte_list, ord(character)) for character in generate_ascii()]
  xor_strings = [''.join(list(map(chr, integer))) for integer in xor_bytes]
  key = detect_key(xor_strings)
  return key

def find_vignere_key(txt):
  """ Determine the vignere cipher key that was used to encrypt an input text """
  key_size = find_key_size(txt)
  transposed_bytes = transpose(txt, key_size)
  vignere_key = ''.join([find_xor_key(x) for x in transposed_bytes])
  return vignere_key

def decrypt_vignere(ciphertext, key):
  """ Decrypt with a vignere cipher given a ciphertext and a key as input """
  bytes_text = b64decode(ciphertext)
  bytes_key = convert(key)
  decrypted_bytes = [b ^ bytes_key[i % len(bytes_key)] for i, b in enumerate(bytes_text)]
  decrypted_characters = [chr(b) for b in decrypted_bytes]
  decrypted_text = ''.join(decrypted_characters)
  return decrypted_text

def test():
  """ Test Challenge 6 """
  ciphertext = remote()
  key = find_vignere_key(ciphertext)
  assert key == 'Terminator X: Bring the noise', 'incorrect key'
  message = decrypt_vignere(ciphertext, key)
  print(key)
  print(message)
  return (key, message)

if __name__ == "__main__":
  test()
