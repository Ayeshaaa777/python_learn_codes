# scope = the region that a variable is recognized
# we have both local and global versions of a single variable

name = "Bro"  # global scope can be accessed anywhere


def display_name():
    name = "ayesha"
    print(name)  # local scope - available only inside the function


display_name()
print(name)


# LEGB order - order in which python will look up names
