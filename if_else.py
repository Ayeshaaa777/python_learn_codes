age = int(input("how old are you?"))
if age >= 18:
    print("you are an adult: ")
elif age == 100:
    print("you are a century old")
elif age < 0:
    print("you havent been born yet")
else:
    print("you are a child")
