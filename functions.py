# function = a block of code which is executed only when it is called
def hello(name, last_name, age):
    print("hello "+name+last_name)
    print("you are"+str(age)+"years old")  # where name is a parameter
    print("how are you")


my_name = "hi"
last_name = "hello"
hello("ayesha", "sami", 17)
hello("bro", "sis", 19)
hello(my_name, last_name, 20)
