# *args = use it when we dont know the number of varying parameters that are to be used
# imp
# args accept a varying amount of positional arguments and pack them into a tuple
def add(*numbers):
    # tuples can be iterable
    sum = 0
   #  numbers[0] = 0 -- cant do this since tuples arent mutable always remember this

    # type cast it into smth changeable
    numbers = list(numbers)
    numbers[0] = 0
    for i in numbers:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6, 7, 8))
