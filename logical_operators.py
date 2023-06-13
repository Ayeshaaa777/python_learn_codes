temp = int(input("what is the temperature outside?: "))
if temp >= 0 and temp <= 30:
    print("the temp is good today")
elif temp < 0 or temp > 30:
    print("the temp is bad today")
