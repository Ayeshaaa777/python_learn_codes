# padding = spacing and alignment
name = "ayesha"
print("Hello my name is {}".format(name))
# for keyword argument.. wtv u pass {name:10} here 0 in place of name  is that keyword argument
print("Hello my name is {0:10}.nice to meet you".format(name))
print("Hello my name is {:<10}.nice to meet you".format(name))
print("hello my name is {:>10}.nice to meet you".format(name))  # right align
print("hello my name is {:^10}. nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))  # binary representation
print("the number is {:o}".format(number))  # octal representation
print("the number is {:X}".format(number))  # hexadecimal number
print("the number is {:E}".format(number))  # scientific notation
