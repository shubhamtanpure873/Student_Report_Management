# LIST PROGRAMS
# Student-related examples for Python Unit 2

subjects = ["Python", "Mathematics", "Physics"]
marks = [86, 78, 91]
attendance = [92, 88, 95]

print("Original subjects:", subjects)

# Indexing
print("First subject:", subjects[0])

# Traversal
print("\nTraversal:")
for subject in subjects:
    print(subject)

# append()
subjects.append("English")

# insert()
subjects.insert(1, "Chemistry")

# extend()
subjects.extend(["DSA", "C"])

# remove()
subjects.remove("C")

# pop()
removed_subject = subjects.pop()
print("\nPopped subject:", removed_subject)

# index()
print("Index of Python:", subjects.index("Python"))

# count()
subjects.append("Python")
print("Count of Python:", subjects.count("Python"))

# sort()
marks.sort()
print("Sorted marks:", marks)

# reverse()
marks.reverse()
print("Reversed marks:", marks)

# list comprehension
long_subjects = [subject for subject in subjects if len(subject) > 5]
print("Long subject names:", long_subjects)

# clear()
temporary_list = ["A", "B", "C"]
temporary_list.clear()
print("After clear():", temporary_list)
