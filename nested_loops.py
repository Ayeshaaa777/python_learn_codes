# the inner loop will finish all of its iterations before finishing one iteration of its outer loop
'''rows = int(input("how many rows?: "))
column = int(input("how many columns?: "))
symbol = input("enter a symbol to use: ")

for i in range(rows):
    for j in range(column):
        print(symbol, end="")
    print()'''
'''pattern 1 '''
rows = int(input("number of rows?: "))
column = int(input("number of columns?: "))
for i in range(rows):
    for j in range(1, column+1):
        print(j, end="")
    print()
