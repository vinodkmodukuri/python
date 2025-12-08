# Python Built-in Data Types - Notes and Examples

# ------------------------------
# 1. Text Type: str
# ------------------------------
name = "Krishna"
print(name)
print(type(name))  # <class 'str'>

# Notes:
# - Strings store text
# - Written inside quotes
# - Immutable (cannot modify directly)

# ------------------------------
# 2. Numeric Types: int, float, complex
# ------------------------------
x = 20         # int (whole number)
y = 10.25      # float (decimal number)
z = 3j         # complex number (3 imaginary)

print(x, type(x))  # int
print(y, type(y))  # float
print(z, type(z))  # complex

# ------------------------------
# 3. Sequence Types: list, tuple, range
# ------------------------------
# List - ordered, mutable
fruits_list = ["apple", "banana", "cherry"]
print(fruits_list)
print(type(fruits_list))

# Tuple - ordered, immutable
fruits_tuple = ("apple", "banana", "cherry")
print(fruits_tuple)
print(type(fruits_tuple))

# Range - sequence of numbers
t = range(10)  # 0 to 9
print(t)
print(type(t))

# ------------------------------
# 4. Mapping Type: dict
# ------------------------------
student = {"name": "Kumar", "Number": "12"}
print(student)
print(type(student))

# Notes:
# - Stores key-value pairs
# - Mutable
# - Keys must be unique

# ------------------------------
# 5. Boolean Type: bool
# ------------------------------
status = True
print(status)
print(type(status))  # bool

# Notes:
# - Only True or False
# - Used in conditions and logic
