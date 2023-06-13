# keyword arguments = arguments preceded by an identifier when we pass them to a function, the order of the arguments doesnt matter unlike positional arguments python knows thge names of the arguments that our functions recieves

# example of positional arguments
def hello(first, middle, last):
    print("hello " + first + " "+middle+" " + last)


hello("bro", "dude", "code")
hello("ayesha", "ammi", "abba")

# example of keyword arguments -- they have an identifier before


def hello(first, middle, last):
    print("hello " + first + " "+middle+" " + last)


# keyword where the order doesnt matter
hello(middle="gpt", last="bard", first="bing")
