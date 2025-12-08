#Bitwise Operators 
# Bitwise operators perform operations on binary representations of integers.
# They operate at the bit level, manipulating individual bits of the numbers.
# Example usage:
a = 5  # In binary: 0101
b = 3  # In binary: 0011

print(a & b)  # Bitwise AND: 0101 & 0011 = 0001 (1 in decimal)
print(a | b)  # Bitwise OR:  0101 | 0011 = 0111 (7 in decimal)
print(a ^ b)  # Bitwise XOR: 0101 ^ 0011 = 0110 (6 in decimal)
print(~a)  # Bitwise NOT: ~0101 = 1010 (-6 in decimal, two's complement)
print(a << 1)  # Left Shift: 0101 << 1 = 1010 (10 in decimal)
print(a >> 1)  # Right Shift: 0101 >> 1 = 0010 (2 in decimal)   
