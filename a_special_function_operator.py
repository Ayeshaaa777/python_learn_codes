import math
x = float(input("enter the number for which u want to find the square root"))


def f(x) -> float:
    y = math.sqrt(x)
    return y


print(f(x))

# here -> , whatever is written after -> it gives the return type or specifies the return type of the function
