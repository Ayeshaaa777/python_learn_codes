# slicing = [start:stop:step]
name = "bro code"
first_name = name[0:3]
print(first_name)
last_name = name[4:8]
print(last_name)
funky_name = name[::3]
print(funky_name)
reverse_name = name[::-1]
print(reverse_name)
website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])
