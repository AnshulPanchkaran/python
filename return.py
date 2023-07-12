


#                         EXAMPLE 1
'''from math import *
def cube(num):
    return pow(int(num),int(3))
   
print(cube(input("enter the number ")))'''


#                       EXAMPLE 2
def cube(num1, num2):
    print(num2 + " of the number  " + num1 + " is ")

    return pow(int(num1),int(num2))

result =cube(input("enter the number you want to be multiplied --->  "), input("enter the number what task you want to perform ---> "))
print( result)