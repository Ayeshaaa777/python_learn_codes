# exception = detecting the problem beforehand which could interrupt the flow of the problem

try:
    numerator = int(input("Eter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")
except ValueError as e:
    print(e)
    print("enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(result)
finally:
    print("this will always execute ")
