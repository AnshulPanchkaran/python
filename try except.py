

try:
    value = 10/0

    number = int(input(" enter the number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")