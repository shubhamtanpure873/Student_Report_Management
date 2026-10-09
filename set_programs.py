# SET PROGRAMS
# Student-related examples for Python Unit 2

departments = {"CSE", "AI&DS", "ECE"}
subjects = {"Python", "Maths", "Physics"}
clubs = {"Coding Club", "Robotics Club"}

print("Departments:", departments)

# add()
clubs.add("AI Club")
print("After add():", clubs)

# remove()
clubs.remove("AI Club")
print("After remove():", clubs)

# discard()
clubs.discard("Photography Club")
print("discard() completed safely.")

# Membership testing
print("CSE in departments:", "CSE" in departments)

# Union
set_a = {"Python", "Maths", "Physics"}
set_b = {"Python", "Chemistry", "Physics"}

print("Union:", set_a.union(set_b))

# Intersection
print("Intersection:", set_a.intersection(set_b))

# Difference
print("Difference:", set_a.difference(set_b))

# Duplicate removal
department_list = ["CSE", "ECE", "CSE", "AI&DS", "ECE"]
unique_departments = set(department_list)
print("After duplicate removal:", unique_departments)
