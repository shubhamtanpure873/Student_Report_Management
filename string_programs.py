# STRING PROGRAMS
# Student-related examples for Python Unit 2

name = "  prathamesh borade  "
department = "computer science"
email = "student@example.com"

print("Original:", name)

# Indexing
print("First character:", name.strip()[0])

# Slicing
print("First five characters:", name.strip()[0:5])

# Concatenation
print("Student: " + name.strip())

# f-string
print(f"Name: {name.strip().title()}, Department: {department.title()}")

# String methods
print("upper():", department.upper())
print("lower():", department.lower())
print("title():", department.title())
print("capitalize():", name.strip().capitalize())
print("strip():", name.strip())

subjects_text = "Python,Maths,Physics"

# split()
subjects = subjects_text.split(",")
print("split():", subjects)

# join()
print("join():", " | ".join(subjects))

# replace()
print("replace():", name.strip().replace("borade", "BORDE"))

# find()
print("find():", name.lower().find("borade"))

# count()
print("count():", name.lower().count("a"))

# startswith()
print("startswith():", email.startswith("student"))

# endswith()
print("endswith():", email.endswith(".com"))


def valid_email(value):
    return "@" in value and "." in value.split("@")[-1]


print("Email valid:", valid_email(email))
