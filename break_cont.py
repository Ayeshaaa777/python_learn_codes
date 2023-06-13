# loop control statements - change a loops execution from its normal seq
# break= used to terminate loop entirely, continue= skips to the next iteration,pass=does nothing, acts as a placeholder
# BREAK
while True:
    name = input("enter your name: ")
    if name != "":
        break
phone_number = "123-456-780"
# CONTINUE
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
# PASS
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
