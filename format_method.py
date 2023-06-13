# str.format() = optional method that gives users more control when displaying output , placeholder method basically
# method 1
animal = " cow "
item = " moon "
text = "The {} jumped over {}"
# print(text.format(animal, item))

# method 2
print("The {0} jumped over {1} ". format(animal, item))  # positional argument

# default method
print("The {} jumped over {} ".format(animal, item))

# method 3 #when variables arent declared beforehand
print("The {animal} jumped over {item}".format(
    animal="cow", item="moon"))  # keyword argument
