# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varying amount of keyword arguments

# * args pack them into a tuple, **kwargs packs them into a dictionary

'''def hello(first, last):
    print("Hello "+first + " "+last)


hello(first="Ayesha", middle="mohammed", last="sami")'''
# CONSOLE PRINTS ERROR
# BCUZ HELLO FUNCTION DIDNT HAVE MIDDLE IN THE FIRST PLACE
# USE KRWARGS TO PRINT AND PASS ANY NUMBER OF ARGUMENTS
# def hello(**kwargs) --> can put up any name


def hello(**kwargs):
    print("Hello "+kwargs['first'] + " " + kwargs['last'])


hello(first="Ayesha", middle="mohammed", last="sami")

# if u want to print everything that has been typed so far


def hello(**names):
    print("Hello ", end=" ")
    for key, value in names.items():
        print(value, end=" ")


hello(title="mrs", first="mohammed", middle="ayesha", last="sami")
