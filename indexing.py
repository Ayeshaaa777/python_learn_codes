# index operator [] = gives access to sequenece's elements (str,list,tuples)
name = "bro Code!"
if (name[0].islower()):
    name = name.capitalize()

print(name[:3])

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]
print(first_name)
print(last_name)
print(last_character)

list = ["hi", "9"]
list.append("hey")
print(list)
print(list[:3])  # 3 is exclusive

tuple = ("hey", "woman", "pie", "8")
print(tuple[-2])
