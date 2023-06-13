import os

path = "C:\\Users\\ayesh\\OneDrive\\Desktop"

if os.path.exists(path):
    print("That location exists!")  # only to check if it exists
    if os.path.isfile(path):
        print("that ois a file")
    elif os.path.isdir(path):
        print("that is a directory! ")
else:
    print("That location doesnt exist")
