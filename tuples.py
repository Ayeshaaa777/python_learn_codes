# tuples = ordered and unchangeable, not mutable
student = ("Bro", 19, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x, end="")

if "Bro" in student:
    print("Bro is here")
