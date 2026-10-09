# DICTIONARY PROGRAMS
# Complete student profile example

student = {
    "roll_number": ("101",),
    "registration_number": ("REG2026001",),
    "date_of_birth": (15, 8, 2006),
    "name": "Aarav Sharma",
    "department": "CSE",
    "subjects": ["Python", "Mathematics", "Physics"],
    "marks": [86, 78, 91],
    "attendance": [92, 88, 95],
    "contact": {
        "address": "Pune, Maharashtra",
        "email": "aarav@example.com"
    },
    "clubs": {"Coding Club", "Robotics Club"}
}

# Accessing values
print("Name:", student["name"])
print("Department:", student["department"])

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:")
for key, value in student.items():
    print(key, ":", value)

# get()
print("Department using get():", student.get("department"))

# update()
student.update({"department": "AI&DS"})
print("Updated department:", student["department"])

# pop()
removed = student.pop("contact")
print("Removed contact:", removed)

# popitem() on a temporary dictionary
temporary = {"A": 1, "B": 2}
print("popitem():", temporary.popitem())

# clear() on a temporary dictionary
temporary.clear()
print("After clear():", temporary)
