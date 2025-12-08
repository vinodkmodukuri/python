# String Slicing Examples

first_name = "Vinod Kumar"

# ------------------------------
# Basic Slicing
# ------------------------------
# Get characters from position 1 to 4 (index 1 to 3)
print(first_name[1:4]) #ino

# Get the first 5 characters (0 to 4)
print(first_name[:5]) #vinod

# Get characters from position 4 to the end
print(first_name[4:]) #d Kumar

# ------------------------------
# Reverse Slicing
# ------------------------------
# Reverse the string
print(first_name[::-1]) #ramuK doniV

# Get characters from end to start skipping 1 step
print(first_name[::-2]) #rmKdnV

# ------------------------------
# Step Slicing
# ------------------------------
# Get every 2nd character from the string
print(first_name[::2]) #VndKmr

# Get characters from index 1 to 8 with step 2
print(first_name[1:8:2]) #io u