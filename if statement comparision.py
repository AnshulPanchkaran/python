def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
      print("number 1 is greater that is")
      return num1
    elif num2 >= num1 and num2>=num3:
     print("number 2 is greater that is ")
     return num2
    else:
      print("number 3 is greater that is ")
      return num3
    
print(max_num(input("enetr first number"), input("enter second number") , input("enter third number ")))