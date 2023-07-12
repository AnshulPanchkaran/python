num1 = float(input("enter first number "))
operator = input(" enter the operation you want to perform on numbers ")
num2 = float(input("enter second number "))

if operator == "+":
    print(" you perform addition and answer is: ")
    print(num1 + num2)
elif operator == "-":
    print(" you perform subtraction and answer is: ")
    print(num1 - num2)
elif operator == "*":
    print(" you perform multiplication and answer is: ")
    print(num1 * num2)
elif operator == "/":
    print(" you perform division and answer is: ")
    print(num1 / num2)
else:
    print("invalid operation")
