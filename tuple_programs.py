# TUPLE PROGRAMS
# Student-related examples for Python Unit 2

# Tuple creation
roll_number = ("101",)
registration_number = ("REG2026001",)
date_of_birth = (15, 8, 2006)

print("Roll number:", roll_number)
print("Registration number:", registration_number)
print("DOB:", date_of_birth)

# Indexing
print("DOB day:", date_of_birth[0])

# Packing
student_identity = ("101", "REG2026001", (15, 8, 2006))
print("Packed tuple:", student_identity)

# Unpacking
roll, registration, dob = student_identity
print("Roll:", roll)
print("Registration:", registration)
print("DOB:", dob)

# count()
print("Count of 101:", roll_number.count("101"))

# index()
print("Index of REG2026001:", student_identity.index("REG2026001"))

# Immutability
# roll_number[0] = "102"
# The above statement would produce TypeError.
print("Tuples are immutable.")
