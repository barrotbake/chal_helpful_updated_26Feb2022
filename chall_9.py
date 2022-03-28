def pkcs7_pad(message, block_size):
    if len(message) == block_size:
        return message
    ch = block_size - len(message) % block_size
    return message + bytes([ch] * ch)

def is_padded(binary_data):
    padding = binary_data[-binary_data[-1]:]
    return all(padding[b] == len(padding) for b in range(0, len(padding)))

def pkcs7_unpad(data):
    if len(data) == 0:
        raise Exception("The input data must contain at least one byte")

    if not is_padded(data):
        return data

    padding_len = data[len(data) - 1]
    return data[:-padding_len]

def main():
    message = b"YELLOW SUBMARINE"
    pad = pkcs7_pad(message, 20)
    print(pad)

if __name__ == "__main__":
    main()