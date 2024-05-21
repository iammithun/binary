def encode_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def decode_from_binary(binary_string):
    binary_values = binary_string.split()
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_characters)

original_text = "Hello"
encoded_text = encode_to_binary(original_text)
decoded_text = decode_from_binary(encoded_text)

print(f"Original text: {original_text}")
print(f"Encoded text: {encoded_text}")
print(f"Decoded text: {decoded_text}")
