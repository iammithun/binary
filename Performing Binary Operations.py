a = 0b1010  # 10 in decimal
b = 0b1100  # 12 in decimal

binary_and = a & b
binary_or = a | b
binary_xor = a ^ b
binary_not = ~a

print(f"a AND b: {bin(binary_and)}")
print(f"a OR b: {bin(binary_or)}")
print(f"a XOR b: {bin(binary_xor)}")
print(f"NOT a: {bin(binary_not & 0b1111)}")  # Masking to show only 4 bits
