# list = used to store multiple items in a single variable
# mutable = changeable
# lists are mutable
# functions of lists
# fuctions like
# food.append(),food.remove(),food.pop()#pop the last element,food.insert()# add it in a position,food.sort(),food.clear()

food = ["biryani", "rice", "dosa"]
food[0] = "sushi"
print(food[0])

food.append("ice cream")
for x in food:
    print(x, end=' ')
food.remove("rice")
for x in food:
    print(x, end=' ')
food.pop()  # will pop the last element
print(food)
food.insert(0, "cake")
print(food)
food.sort()
# sorts alphabetically
food.clear()
print(food)
