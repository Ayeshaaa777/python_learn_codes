import time
# for loop is a statement that will execute a limited number of times -- in this we will code a countdown
# while loop = unlimited , for loop = limited
# for i in range(10):
#  print(i+1)
# for i in range(50, 100):
# print(i)
# 50 is inclusive and 100 is exclusive
# for i in range(50, 100+1, 2):
# print(i)
# for i in "Bro Code":
# print(i)
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("happy new year!")
