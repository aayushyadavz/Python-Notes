course_name = "  python programming   "

print(course_name.upper())  # PYTHON PROGRAMMING
print(course_name.lower())  # python programming
# print(course_name.strip())  # removes the white spaces
print(course_name.lstrip())  # removes the white spaces from left side
print(course_name.rstrip())  # removes the white spaces from right side
print(course_name.title())  # Python Programming
print(course_name.find("pro"))  # 9
print(course_name.replace("p", "j"))  # jython jrogramming
print("pro" in course_name)  # True
print("swift" not in course_name)  # True

# Note: These methods return a new string without affecting the original one.
